#!/usr/bin/env python3
# Find where the Corpus section actually ends

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    content = f.read()

# Find the position of "id: \"corpus\"" (line 15998)
lines = content.split('\n')
corpus_line = None
for i, line in enumerate(lines):
    if 'id: "corpus"' in line:
        corpus_line = i
        break

print(f"Found 'id: corpus' at line {corpus_line + 1}")

# Now find where this section ends by counting brackets from this line
brace_count = 0
paren_count = 0
in_string = False
string_char = None
escape_next = False

for i in range(corpus_line, len(lines)):
    line = lines[i]
    for j, char in enumerate(line):
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
    
    # Print state at interesting points
    if i >= corpus_line and i <= corpus_line + 3:
        print(f"Line {i+1}: brace={brace_count}, paren={paren_count}")
    
    # Check if we've returned to balanced (after some opening)
    if i > corpus_line + 3 and brace_count == 0 and paren_count == 0:
        print(f"\nSection ends at line {i + 1}")
        print(f"Context:")
        for k in range(max(0, i-3), min(len(lines), i+4)):
            marker = " --> " if k == i else "     "
            print(f"{marker}{k+1}: {lines[k]}")
        break

print(f"\nFinal: brace={brace_count}, paren={paren_count}")
