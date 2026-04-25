#!/usr/bin/env python3
"""分析Ty函数的完整结构"""

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# 找到Ty函数开始
ty_start = None
for i, line in enumerate(lines):
    if 'function Ty()' in line:
        ty_start = i
        break

print(f"Ty function starts at line {ty_start + 1}")

# 找到sections数组开始 - 在Ty函数中
# 应该是 return ( ... children: [
for i in range(ty_start, min(ty_start + 50, len(lines))):
    print(f"{i+1}: {lines[i].rstrip()}")
