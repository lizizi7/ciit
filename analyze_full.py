#!/usr/bin/env python3
# Full file analysis - find all bracket imbalances

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    content = f.read()

lines = content.split('\n')

brace_balance = 0
paren_balance = 0
bracket_balance = 0

print("Scanning entire file for bracket imbalances...\n")

for i, line in enumerate(lines):
    for char in line:
        if char == '(':
            paren_balance += 1
        elif char == ')':
            paren_balance -= 1
        elif char == '{':
            brace_balance += 1
        elif char == '}':
            brace_balance -= 1
        elif char == '[':
            bracket_balance += 1
        elif char == ']':
            bracket_balance -= 1
    
    # Report when balance goes negative
    if paren_balance < 0:
        print(f"NEGATIVE PAREN at line {i+1}: {line.strip()[:60]}")
        paren_balance = 0  # Reset to continue scanning
    if brace_balance < 0:
        print(f"NEGATIVE BRACE at line {i+1}: {line.strip()[:60]}")
        brace_balance = 0
    if bracket_balance < 0:
        print(f"NEGATIVE BRACKET at line {i+1}: {line.strip()[:60]}")
        bracket_balance = 0

print(f"\nFinal balance: braces={brace_balance}, parens={paren_balance}, brackets={bracket_balance}")
