#!/usr/bin/env python3
"""修复JS文件的语法错误"""

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# 找到Ty函数开始
ty_start = None
for i, line in enumerate(lines):
    if 'function Ty()' in line:
        ty_start = i
        break

print(f"Ty function starts at line {ty_start + 1}")

# 从Ty函数往前找第一个o.jsx(
ty_section = None
for i in range(ty_start - 1, 0, -1):
    if 'o.jsx(' in lines[i] and 'section' not in lines[i]:
        ty_section = i
        break

print(f"Ty section starts at line {ty_section + 1}: {lines[ty_section].strip()}")

# 显示Ty section区域
print("\n--- Ty section area ---")
for i in range(max(0, ty_section - 2), min(len(lines), ty_section + 15)):
    print(f"{i+1}: {lines[i].rstrip()}")
