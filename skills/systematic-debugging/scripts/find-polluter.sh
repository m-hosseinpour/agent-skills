#!/usr/bin/env bash
# Sequentially scan test files for the invocation after which a path appears.
# No cleanup or state reset; separate invocations cannot reproduce every race.

set -euo pipefail

usage() {
  cat <<'HELP'
Usage: bash find-polluter.sh <polluted_path> <test_glob> -- <command> [args...]

Run from an approved disposable project workspace with the target path absent.
Supply a verified runner command for ONE test file; no runner is autodetected.
A standalone {} argument is replaced by the file, else the file is appended.
Commands are argv, not shell expressions: use a wrapper for pipes or redirects.
The test glob is relative to this workspace; Bash ** is enabled, dotfiles excluded.
Symlinked test files and directories resolving outside the workspace are rejected.

Examples:
  bash find-polluter.sh 'unexpected.db' 'tests/**/test_*.py' -- uv run pytest '{}'
  bash find-polluter.sh 'unexpected-cache' 'src/**/*.test.ts' -- npm test --

Requires Bash 4+. Output and runner status are preserved; artifacts are left intact.
Exit: 0 = no target appeared and all invocations succeeded; 1 = target appeared;
      2 = invalid setup or inconclusive execution. A hit is not proof of root cause.
HELP
}

fail() {
  printf 'error: %s\n' "$1" >&2
  exit 2
}

if [[ ${1:-} == --help ]]; then
  usage
  exit 0
fi
if (( $# < 4 )); then
  usage >&2
  exit 2
fi
(( BASH_VERSINFO[0] >= 4 )) || fail 'Bash 4 or newer is required.'
[[ $3 == -- ]] || fail 'Pass the runner after -- as separate arguments, not a command string.'

POLLUTED_PATH=$1
TEST_PATTERN=${2#./}
shift 3
RUNNER=("$@")
[[ -n $POLLUTED_PATH && -n $TEST_PATTERN && -n ${RUNNER[0]} ]] || fail 'Paths, pattern, and command must not be empty.'
case "$TEST_PATTERN" in
  /*|..|../*|*/../*|*/..) fail 'Test glob must stay within the current workspace.' ;;
esac
[[ ! -e $POLLUTED_PATH && ! -L $POLLUTED_PATH ]] || fail "'$POLLUTED_PATH' already exists. Preserve it; use a fresh approved workspace or ask before removing it."

for arg in "${RUNNER[@]}"; do
  [[ $arg != *'{}'* || $arg == '{}' ]] || fail '{} must be a standalone argument.'
done

shopt -s nullglob globstar
# Disable word splitting, but allow pathname expansion for the user-supplied glob.
IFS=''
# shellcheck disable=SC2206
CANDIDATES=( ./$TEST_PATTERN )
TEST_FILES=()
for file in "${CANDIDATES[@]}"; do
  [[ ! -f $file ]] || TEST_FILES+=("$file")
done
(( ${#TEST_FILES[@]} > 0 )) || fail 'No test files matched; check the pattern.'

WORKSPACE_ROOT=$(pwd -P)
WORKSPACE_PREFIX=${WORKSPACE_ROOT%/}/
validate_file() {
  local file=$1 directory
  [[ ! -L $file ]] || fail "Symlinked test files are not supported: '$file'."
  [[ -f $file ]] || fail "Test file is no longer available: '$file'."
  directory=$(cd -P -- "${file%/*}" && pwd -P) || fail "Cannot resolve test directory for '$file'."
  [[ "$directory/" == "$WORKSPACE_PREFIX"* ]] || fail "Test directory resolves outside the workspace: '$file'."
}

# Check the whole selection before running anything, then catch changes by runners.
# This is not isolation against malicious test code or concurrent filesystem races.
for file in "${TEST_FILES[@]}"; do
  validate_file "$file"
done

printf 'Target: %s\nSelected test files: %s\n' "$POLLUTED_PATH" "${#TEST_FILES[@]}"
COUNT=0
for file in "${TEST_FILES[@]}"; do
  validate_file "$file"
  COUNT=$((COUNT + 1))
  COMMAND=()
  HAS_PLACEHOLDER=0
  for arg in "${RUNNER[@]}"; do
    if [[ $arg == '{}' ]]; then
      COMMAND+=("$file")
      HAS_PLACEHOLDER=1
    else
      COMMAND+=("$arg")
    fi
  done
  (( HAS_PLACEHOLDER )) || COMMAND+=("$file")
  printf '\n[%s/%s] %s\nRunning: ' "$COUNT" "${#TEST_FILES[@]}" "$file"
  printf '%q ' "${COMMAND[@]}"
  printf '\n'

  STATUS=0
  "${COMMAND[@]}" || STATUS=$?
  printf 'Runner exit status: %s\n' "$STATUS"
  if [[ -e $POLLUTED_PATH || -L $POLLUTED_PATH ]]; then
    printf 'Target appeared after: %s\nArtifact preserved: %s\n' "$file" "$POLLUTED_PATH"
    printf 'Earlier invocations may have supplied prerequisite state; trace before assigning cause.\n'
    exit 1
  fi
  (( STATUS == 0 )) || fail "Runner failed for '$file'; no conclusion about later files."
done

printf '\nNo target path appeared; all selected invocations succeeded.\n'
printf 'This does not rule out other pollution or order/process/concurrency-dependent failures.\n'
