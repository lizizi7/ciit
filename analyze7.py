#!/usr/bin/env python3
# Count parentheses and braces precisely for the Corpus section

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.read().split('\n')

# Corpus section starts at line 15996
start = 15995  # 0-indexed

# End is where node says the error is (16340) or we can scan further
# Let's scan up to 200 lines

paren_open = 0
paren_close = 0
brace_open = 0
brace_close = 0

print("Scanning from line 15996 to 16350...\n")

for i in range(start, min(start + 200, len(lines))):
    line = lines[i]
    line_open_p = line.count('(')
    line_close_p = line.count(')')
    line_open_b = line.count('{')
    line_close_b = line.count('}')
    
    paren_open += line_open_p
    paren_close += line_close_p
    brace_open += line_open_b
    brace_close += line_close_b
    
    net_p = paren_open - paren_close
    net_b = brace_open - brace_close
    
    if net_p != 0 or net_b != 0 or 'corpus' in line or 'const my' in line:
        print(f"{i+1:5d}: +({line_open_p}-{line_close_p}) +({line_open_b}-{line_close_b}) | net_p={net_p:3d} net_b={net_b:3d} | {line.strip()[:60]}")
    
    if 'const my' in line:
        print(f"\nFound 'const my' at line {i+1}")
        print(f"Final: open_p={paren_open}, close_p={paren_close}, net_p={net_p}")
        print(f"       open_b={brace_open}, close_b={brace_close}, net_b={net_b}")
        break
