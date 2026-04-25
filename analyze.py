#!/usr/bin/env python3
import re

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# Find the corpus section start (line 15996)
section_start = 15995  # 0-indexed
section_end = 16340  # Find where section ends

# Extract section content
section_lines = lines[section_start:section_end+1]
section_code = ''.join(section_lines)

# Count brackets
brace_count = section_code.count('{') - section_code.count('}')
paren_count = section_code.count('(') - section_code.count(')')

print(f"Section from line {section_start+1} to {section_end}")
print(f"Code snippet:")
print(''.join(section_lines[-10:]))
print(f"\nBrace balance ({{ }}) mismatch: {brace_count}")
print(f"Paren balance (( )) mismatch: {paren_count}")

# Also check for the children array
print("\n\nLooking for children array end...")
# Find where the children array of o.jsxs("div", { might end
# children: [
#   ... content ...
# ]
# }),

# Find the last ], that closes the main children array
content_after_children = section_code[section_code.find('children: ['):]
print(f"children array closes at position: {content_after_children.rfind('],')}")
