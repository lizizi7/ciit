#!/usr/bin/env python3
"""分析section函数归属"""

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# 找到所有函数和section
functions = []
for i, line in enumerate(lines):
    if 'function ' in line and '(' in line and ')' in line and '{' in line:
        # 提取函数名
        match = line.strip().split('(')[0].replace('function ', '')
        if len(match) <= 5 and match.isalpha():  # 简单函数名
            functions.append((i, match))

print("Functions:")
for i, name in functions:
    print(f"  Line {i+1}: {name}")

print("\n\nSections:")
sections = []
for i, line in enumerate(lines):
    if 'o.jsx("section"' in line:
        # 找id
        id_match = None
        for j in range(i, min(i+5, len(lines))):
            if 'id: "' in lines[j]:
                start = lines[j].find('id: "') + 5
                end = lines[j].find('"', start)
                if start > 4:
                    id_match = lines[j][start:end]
                break
        sections.append((i, id_match))
        print(f"  Line {i+1}: {id_match}")

# 分析section属于哪个函数
print("\n\nSection to Function mapping:")
for sec_line, sec_id in sections:
    # 找最近的之前的函数
    prev_func = None
    for func_line, func_name in functions:
        if func_line < sec_line:
            prev_func = (func_line, func_name)
    if prev_func:
        print(f"  {sec_id} (line {sec_line+1}) -> {prev_func[1]} (line {prev_func[0]+1})")
