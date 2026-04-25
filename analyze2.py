#!/usr/bin/env python3
import re

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    content = f.read()

# Find all sections
sections = []
for m in re.finditer(r'o\.jsx\("section", \{', content):
    sections.append(m.start())

print(f"Found {len(sections)} sections at positions: {sections}")

# Check the problematic section (15996 line = position in file)
# Let's find the exact position
with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# Line 15996 is 0-indexed line 15995
section_line = 15995
print(f"\nSection starts at line {section_line + 1}:")
print(lines[section_line])

# Let's count brackets from this line onwards
brace_count = 0
paren_count = 0
bracket_count = 0

# Find the end of this section
for i in range(section_line, min(section_line + 500, len(lines))):
    line = lines[i]
    # Count all brackets (not just at line start)
    for char in line:
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
        elif char == '(':
            paren_count += 1
        elif char == ')':
            paren_count -= 1
        elif char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
    
    # Check if we're balanced (at section boundary)
    if brace_count == 0 and paren_count == 0 and i > section_line:
        print(f"\nSection appears to end at line {i + 1}")
        print(f"Lines {i-2} to {i+2}:")
        for j in range(i-2, i+3):
            if j < len(lines):
                print(f"{j+1}: {lines[j].rstrip()}")
        break

print(f"\nFinal counts: braces={brace_count}, parens={paren_count}, brackets={bracket_count}")
