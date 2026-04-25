#!/usr/bin/env python3
# Trace bracket nesting to find exact section boundaries

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    content = f.read()

lines = content.split('\n')

# Find "id: corpus" line
corpus_line = None
for i, line in enumerate(lines):
    if 'id: "corpus"' in line:
        corpus_line = i
        break

print(f"Corpus section header at line {corpus_line + 1}: {lines[corpus_line].strip()}")

# Track all bracket positions
brace_stack = []  # Stack of (line, col, char)
paren_stack = []

in_string = False
string_char = None
escape_next = False

# Find the section opening
# Look for "o.jsx("section", {" before corpus line
for i in range(corpus_line - 5, corpus_line + 1):
    if 'o.jsx("section", {' in lines[i] or "o.jsx('section', {" in lines[i]:
        print(f"Section opens at line {i + 1}: {lines[i].strip()}")
        break

# Now trace from section start to find where it closes
# We need to find the matching '})' for the 'o.jsx("section", {'

# Simple approach: find where the pattern "    })" appears after section start
# and the count of { } and ( ) returns to 0

# Find the exact line where "o.jsx("section", {" ends (the {)
# That line is at corpus_line - 2 (checking)

# Let me find the o.jsx("section", { line
section_start = None
for i in range(corpus_line - 10, corpus_line + 1):
    if 'o.jsx("section", {' in lines[i]:
        section_start = i
        break

if section_start is None:
    for i in range(corpus_line - 10, corpus_line + 1):
        if "section" in lines[i] and "o.jsx" in lines[i]:
            section_start = i
            break

print(f"\nAnalyzing from line {section_start + 1}...")

# Count brackets from section_start
brace_depth = 0
paren_depth = 0
max_brace = 0
max_paren = 0

for i in range(section_start, min(section_start + 500, len(lines))):
    line = lines[i]
    for char in line:
        if char == '{':
            brace_depth += 1
        elif char == '}':
            brace_depth -= 1
        elif char == '(':
            paren_depth += 1
        elif char == ')':
            paren_depth -= 1
    
    # Track max depth
    max_brace = max(max_brace, brace_depth)
    max_paren = max(max_paren, paren_depth)
    
    # Check if we're back to start level
    if brace_depth == 0 and paren_depth == 0 and i > section_start + 3:
        print(f"\nSection closes at line {i + 1}")
        print(f"Context:")
        for k in range(max(0, i-5), min(len(lines), i+3)):
            marker = " --> " if k == i else "     "
            print(f"{marker}{k+1}: {lines[k]}")
        break

print(f"\nMax nesting: braces={max_brace}, parens={max_paren}")
