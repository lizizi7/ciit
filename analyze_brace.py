#!/usr/bin/env python3
# Track brace balance throughout file

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    content = f.read()

lines = content.split('\n')

brace_balance = 0
max_brace = 0

print("Tracking brace balance...\n")

for i, line in enumerate(lines):
    for char in line:
        if char == '{':
            brace_balance += 1
        elif char == '}':
            brace_balance -= 1
    
    max_brace = max(max_brace, brace_balance)
    
    # Report key points
    if brace_balance == 1 and i < 100:
        print(f"First reach brace=1 at line {i+1}: {line.strip()[:50]}")
    if brace_balance == 0 and i > 15350 and i < 15500:
        print(f"Back to brace=0 at line {i+1}: {line.strip()[:50]}")
    if i > len(lines) - 50:
        print(f"Line {i+1}: brace={brace_balance}: {line.strip()[:50]}")

print(f"\nFinal balance: {brace_balance}, Max: {max_brace}")
