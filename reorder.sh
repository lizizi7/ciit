#!/bin/bash

# Section行范围
# 1. background: 15355-15485 (131行)
# 2. corpus: 15557-15995 (439行)
# 3. analytics: 15996-16460 (465行)
# 4. features: 16461-16757 (297行)
# 5. design: 16758-17117 (360行)
# 6. roadmap: 17118-17585 (468行)
# 7. cases: 17586-17774 (189行) + footer

# 先备份
cp assets/index-D9h_BwJ2.js assets/index-D9h_BwJ2.js.bak

# 使用Python更精确地处理
python3 << 'EOF'
import re

with open('assets/index-D9h_BwJ2.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到所有section的完整代码 - 使用正则匹配
# 每个section以 o.jsx("section", { 开始，以 }); 结束（顶层）
sections = {}

# 使用更智能的方式：找到所有section标签，然后匹配其父级结构
# 但由于是压缩代码，我们按行处理

with open('assets/index-D9h_BwJ2.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 定义section起始行（1-indexed，转换为0-indexed）
section_starts = [15355-1, 15557-1, 15996-1, 16461-1, 16758-1, 17118-1, 17586-1]

# 找到每个section的结束 - 向前找匹配的 });
def find_matching_end(lines, start):
    """从start向前找 o.jsx("section", { 的结束位置"""
    # 这个section应该是以 }) 结束的
    # 我们用括号计数来找
    depth = 0
    in_section = False
    for i in range(start, len(lines)):
        line = lines[i]
        for char in line:
            if char == '{':
                depth += 1
                in_section = True
            elif char == '}':
                depth -= 1
                if in_section and depth == 0:
                    return i + 1  # 返回行号(1-indexed)
    return -1

# 解析sections
section_data = []
for idx, start in enumerate(section_starts):
    end = find_matching_end(lines, start)
    section_data.append((start+1, end, idx+1))  # 转为1-indexed
    print(f"Section {idx+1}: 行{start+1}-{end}")

# 提取section代码
codes = []
for start, end, _ in section_data:
    codes.append(''.join(lines[start-1:end]))

# 按新顺序排列
# 目标: 1,7,2,3,4,5,6
new_order = [0, 6, 1, 2, 3, 4, 5]

# header: 第1行到第一个section之前
# footer: 最后一个section结束后到文件末尾
header_end = section_starts[0]  # 0-indexed
footer_start = section_data[-1][1]  # 1-indexed

new_content = ''.join(lines[:header_end])
for idx in new_order:
    new_content += codes[idx]
new_content += ''.join(lines[footer_start:])

with open('assets/index-D9h_BwJ2.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\n完成section重排序!")
EOF
