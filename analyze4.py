#!/usr/bin/env python3
# Count brackets in section 3 (lines 15996-16340)

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# Count brackets from line 15996 to 16340 (inclusive)
start = 15995  # 0-indexed
end = 16340    # 0-indexed

brace_open = 0
brace_close = 0
paren_open = 0
paren_close = 0

in_string = False
string_char = None
escape_next = False

for i in range(start, end + 1):
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
            brace_open += 1
        elif char == '}':
            brace_close += 1
        elif char == '(':
            paren_open += 1
        elif char == ')':
            paren_close += 1

print(f"From line 15996 to 16340:")
print(f"Opens: {{ = {brace_open}, ( = {paren_open}")
print(f"Closes: }} = {brace_close}, ) = {paren_close}")
print(f"Net braces: {brace_open - brace_close} (should be 0 if balanced)")
print(f"Net parens: {paren_open - paren_close} (should be 0 if balanced)")

# Check the last few lines
print(f"\nLast lines:")
for i in range(max(start, end-5), min(len(lines), end+2)):
    print(f"{i+1}: {lines[i].rstrip()}")
