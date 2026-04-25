#!/usr/bin/env python3
# Analyze the full structure of section 3 (Corpus)

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# Section 3 (Corpus) starts at line 15996 (1-indexed)
start = 15995  # 0-indexed

# Find the end of this section by tracking bracket balance
# We'll count from 0 and find where it returns to 0

brace_count = 0  # {
paren_count = 0  # (
bracket_count = 0  # [

in_string = False
string_char = None
escape_next = False

i = start
while i < len(lines):
    line = lines[i]
    for char in line:
        if escape_next:
            escape_next = False
            continue
        
        if char == '\\' and in_string:
            escape_next = True
            continue
            
        if char in ('"', "'") and not in_string:
            in_string = True
            string_char = char
            continue
            
        if char == string_char and in_string:
            in_string = False
            string_char = None
            continue
            
        if in_string:
            continue
            
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
    
    # Check if we've returned to zero
    if i > start and brace_count == 0 and paren_count == 0 and bracket_count == 0:
        print(f"Section ends at line {i + 1}")
        print(f"Lines {i-2} to {i+3}:")
        for j in range(max(0, i-2), min(len(lines), i+4)):
            marker = " --> " if j == i else "     "
            print(f"{marker}{j+1}: {lines[j].rstrip()}")
        break
    
    i += 1

print(f"\nAt section end: braces={brace_count}, parens={paren_count}, brackets={bracket_count}")

# Now let's look at the structure around the end
print("\n\nContext around section end (16335-16345):")
for j in range(16334, 16345):
    if j < len(lines):
        print(f"{j+1}: {lines[j].rstrip()}")
