#!/usr/bin/env python3
import re

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    content = f.read()
lines = content.split('\n')

# 找到Ty函数（main component）的开始行
ty_start = None
for i, line in enumerate(lines):
    if 'function Ty' in line or 'const Ty = ' in line or line.strip().startswith('function Ty('):
        ty_start = i
        break

if ty_start is None:
    # 查找Ty =
    for i, line in enumerate(lines):
        if 'Ty = (0,' in line or 'Ty=' in line:
            ty_start = i
            break

print(f"Ty function starts at line {ty_start + 1}")

# 查找sections数组开始
sections_start = None
for i, line in enumerate(lines):
    if 'children: [' in line and i > 15300 and i < 15400:
        sections_start = i
        break

print(f"Sections children array starts at line {sections_start + 1}")

# 找到sections数组结束的]
# 查找第一个section开始
first_section_line = None
for i, line in enumerate(lines):
    if 'o.jsx("section"' in line:
        first_section_line = i
        break

print(f"First section at line {first_section_line + 1}")

# 查找最后一个section结束后的]和)
last_section_end = None
for i in range(len(lines) - 1, 15300, -1):
    if '})' in lines[i] and i > first_section_line:
        last_section_end = i
        break

print(f"Last section ends around line {last_section_end + 1}")

# 显示关键区域
print("\n--- Around section end area ---")
for i in range(max(0, last_section_end - 5), min(len(lines), last_section_end + 10)):
    print(f"{i+1}: {lines[i]}")
