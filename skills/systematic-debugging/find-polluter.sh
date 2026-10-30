#!/usr/bin/env bash
# Find which test creates unwanted files or state, by trying each test in turn.
#
# Usage:
#   find-polluter.sh <polluted_path> <test_glob> [test_command]
#
#   polluted_path  file or directory that should NOT exist (the pollution)
#   test_glob      glob of test files to try, e.g. 'tests/**/*.py'
#   test_command   how to run ONE test file; may contain {} as a placeholder
#                  for the file, else the file is appended. Autodetected if
#                  omitted. Set it explicitly for anything non-standard.
#
# Examples:
#   find-polluter.sh '.git'    'src/**/*.test.ts' 'npm test {}'
#   find-polluter.sh 'tmp.db'  'tests/**/test_*.py' 'uv run pytest {}'
#   find-polluter.sh '.cache'  'tests/**/*.py'      # autodetect the runner
#
# The pollution must not exist when you start: if it is already there, the
# script cannot tell which test made it, so it stops and asks you to clean up.
#
# Note: the test command is word-split, so keep it simple and unquoted. A path
# containing spaces is not supported; pass a command that handles the file
# itself (e.g. your own wrapper script) if you need that.

set -euo pipefail

usage() {
  sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-1}"
}

[ $# -ge 2 ] || usage 1

POLLUTION_CHECK="$1"
TEST_PATTERN="${2#./}"
TEST_CMD="${3:-}"

# --- Resolve the test command ------------------------------------------------
if [ -z "$TEST_CMD" ]; then
  if [ -f pyproject.toml ] || [ -f setup.py ] || [ -f setup.cfg ]; then
    if command -v uv >/dev/null 2>&1; then
      TEST_CMD='uv run pytest {}'
    else
      TEST_CMD='python -m pytest {}'
    fi
  elif [ -f package.json ]; then
    TEST_CMD='npm test {}'
  else
    echo "error: could not detect a test runner here." >&2
    echo "       pass one explicitly, e.g.: $0 '$POLLUTION_CHECK' '$TEST_PATTERN' 'uv run pytest {}'" >&2
    exit 1
  fi
fi

# Fail fast: a pre-existing pollution makes the whole search meaningless.
if [ -e "$POLLUTION_CHECK" ]; then
  echo "error: '$POLLUTION_CHECK' already exists." >&2
  echo "       Remove it first, then run again so each test starts clean." >&2
  exit 1
fi

echo "Pollution to find: $POLLUTION_CHECK"
echo "Test pattern:      $TEST_PATTERN"
echo "Test command:      $TEST_CMD"
echo ""

# find emits ./-prefixed paths, so match the pattern with or without ./. Also
# try the pattern with '**/' collapsed: find -path cannot match '**/' against
# zero directory levels, so 'src/**/*.test.ts' would skip 'src/top.test.ts'.
TEST_FILES=$(find . \( -path "./$TEST_PATTERN" -o -path "./${TEST_PATTERN//\*\*\//}" \) | sort -u || true)
if [ -z "$TEST_FILES" ]; then
  TOTAL=0
else
  TOTAL=$(printf '%s\n' "$TEST_FILES" | wc -l | tr -d ' ')
fi
echo "Found $TOTAL test file(s)"
echo ""

if [ "$TOTAL" -eq 0 ]; then
  echo "Nothing to try — check the pattern." >&2
  exit 1
fi

run_one() {
  local file="$1"
  # shellcheck disable=SC2086
  set -- ${TEST_CMD//\{\}/$file}
  if [ "$#" -eq 0 ]; then
    return 0
  fi
  "$@" > /dev/null 2>&1 || true
}

COUNT=0
for TEST_FILE in $TEST_FILES; do
  COUNT=$((COUNT + 1))
  echo "[$COUNT/$TOTAL] $TEST_FILE"
  run_one "$TEST_FILE"

  if [ -e "$POLLUTION_CHECK" ]; then
    echo ""
    echo "FOUND IT: $TEST_FILE"
    echo "  created: $POLLUTION_CHECK"
    echo ""
    ls -la "$POLLUTION_CHECK"
    echo ""
    echo "To investigate:"
    echo "  ${TEST_CMD//\{\}/$TEST_FILE}"
    echo "  \$EDITOR $TEST_FILE"
    exit 1
  fi
done

echo ""
echo "No polluter found — every test ran clean."
exit 0
