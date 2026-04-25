#!/usr/bin/env python3
# Full bracket analysis from line 15996 to end of file

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.read().split('\n')

# Count brackets from section start
start = 15995  # 0-indexed

brace_balance = 0
paren_balance = 0

for i in range(start, len(lines)):
    line = lines[i]
    
    for char in line:
        if char == '(':
            paren_balance += 1
        elif char == ')':
            paren_balance -= 1
        elif char == '{':
            brace_balance += 1
        elif char == '}':
            brace_balance -= 1
    
    # Print key lines
    if i >= 16335 and i <= 16345:
        status = "OK" if brace_balance == 0 and paren_balance == 0 else "IMBALANCED"
        print(f"Line {i+1}: brace={brace_balance:3d}, paren={paren_balance:3d} {status}: {line.strip()[:60]}")
    
    # Stop if we find a const definition after balanced
    if 'const my = [' in line:
        print(f"\nFound 'const my' at line {i+1}")
        print(f"Balance before this line: brace={brace_balance}, paren={paren_balance}")
        break

# Find where the corpus section actually ends
print("\n\nSearching for corpus section end...")

# Look backwards from const my
for i in range(start + 400, start, -1):
    if i < len(lines):
        line = lines[i]
        # Check for section-related closing
        if 'id: "corpus"' in line:
            print(f"Found corpus at line {i+1}")
            break
