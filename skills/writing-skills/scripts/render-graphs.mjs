#!/usr/bin/env node

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { execFileSync } from 'node:child_process';

const usage = 'Usage: node render-graphs.mjs <skill-directory> [--output-dir <directory>]';

function parseArguments(args) {
  let skillDirectory;
  let outputDirectory;
  for (let index = 0; index < args.length; index += 1) {
    const argument = args[index];
    if (argument === '--output-dir') {
      const value = args[index + 1];
      if (outputDirectory !== undefined || !value || value.startsWith('--')) {
        throw new Error(`--output-dir requires one directory.\n${usage}`);
      }
      outputDirectory = value;
      index += 1;
    } else if (argument.startsWith('--') || skillDirectory !== undefined) {
      throw new Error(`Unexpected argument: ${argument}\n${usage}`);
    } else {
      skillDirectory = argument;
    }
  }
  if (!skillDirectory) throw new Error(usage);
  const skillPath = resolve(skillDirectory);
  return {
    skillFile: join(skillPath, 'SKILL.md'),
    outputDirectory: outputDirectory === undefined
      ? join(skillPath, 'diagrams')
      : resolve(outputDirectory),
  };
}

function extractDotBlocks(markdown) {
  const blocks = [];
  let fence;
  let lines = [];
  for (const line of markdown.split(/\r?\n/)) {
    if (fence) {
      const closing = line.match(/^ {0,3}(`{3,}|~{3,})\s*$/);
      if (closing && closing[1][0] === fence.character && closing[1].length >= fence.length) {
        if (fence.isDot) blocks.push(lines.join('\n'));
        fence = undefined;
        lines = [];
      } else if (fence.isDot) {
        lines.push(line);
      }
    } else {
      const opening = line.match(/^ {0,3}(`{3,}|~{3,})(.*)$/);
      if (opening) {
        fence = {
          character: opening[1][0],
          length: opening[1].length,
          isDot: opening[2].trim() === 'dot',
        };
      } else if (/^(?:\s*>\s*)*\s*(?:(?:[-+*]|\d+[.)])\s+)?(?:`{3,}|~{3,})dot\s*$/.test(line)) {
        throw new Error('Container or indented dot fences are unsupported. Move the diagram to a top-level fence (at most three leading spaces).');
      }
    }
  }
  if (fence?.isDot) throw new Error('Unclosed dot code fence in SKILL.md.');
  return blocks;
}

function render(content, index) {
  if (!content.trim()) throw new Error(`Diagram ${index} has empty DOT content.`);
  let svg;
  try {
    svg = execFileSync('dot', ['-Tsvg'], {
      input: content,
      encoding: 'utf8',
      stdio: ['pipe', 'pipe', 'pipe'],
      maxBuffer: 10 * 1024 * 1024,
    });
  } catch (error) {
    if (error.code === 'ENOENT') {
      throw new Error('Graphviz dot is unavailable. Install it through your approved environment setup.');
    }
    const diagnostic = error.stderr?.toString().trim() || error.message;
    throw new Error(`Diagram ${index} failed to render: ${diagnostic}`);
  }
  if ((svg.match(/<svg\b/g) || []).length !== 1 || !svg.trimEnd().endsWith('</svg>')) {
    throw new Error(`Diagram ${index} must contain exactly one renderable graph per dot fence.`);
  }
  return svg;
}

function main() {
  const { skillFile, outputDirectory } = parseArguments(process.argv.slice(2));
  const blocks = extractDotBlocks(readFileSync(skillFile, 'utf8'));
  if (blocks.length === 0) {
    console.log(`No dot code fences found in ${skillFile}.`);
    return;
  }

  // Number by block order: DOT graph names can repeat or be quoted/absent.
  const outputs = blocks.map((_, index) => join(outputDirectory, `diagram-${index + 1}.svg`));
  for (const output of outputs) {
    if (existsSync(output)) throw new Error(`Refusing to overwrite ${output}. Choose a new --output-dir.`);
  }

  // Validate every graph before creating outputs; malformed DOT must not look like partial success.
  const rendered = blocks.map((block, index) => render(block, index + 1));
  mkdirSync(outputDirectory, { recursive: true });
  for (let index = 0; index < outputs.length; index += 1) {
    // Exclusive creation also protects files created after the initial check.
    writeFileSync(outputs[index], rendered[index], { flag: 'wx' });
    console.log(`Rendered: ${outputs[index]}`);
  }
}

try {
  main();
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exitCode = 1;
}
