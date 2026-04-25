#!/usr/bin/env python3
import re

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

# 找到所有section开始的行号
section_lines = []
for i, line in enumerate(lines):
    if 'o.jsx("section"' in line:
        section_lines.append(i)

print(f"找到 {len(section_lines)} 个sections")

# 找到每个section的范围
def find_section_end(content_lines, start):
    """从start行开始，找到匹配的 }) 结束行"""
    depth = 0
    for i in range(start, len(content_lines)):
        line = content_lines[i]
        # 跳过注释行
        stripped = line.strip()
        if stripped.startswith('/*') and '*/' in stripped:
            continue
        if stripped.startswith('//'):
            continue
        for char in line:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0:
                    return i
    return -1

sections = []
for line_num in section_lines:
    # 提取id (在下一行)
    if line_num + 1 < len(lines):
        id_match = re.search(r'id: "([^"]+)"', lines[line_num + 1])
        section_id = id_match.group(1) if id_match else f"section_{len(sections)}"
    else:
        section_id = f"section_{len(sections)}"
    
    end_line = find_section_end(lines, line_num)
    sections.append({
        'id': section_id,
        'start': line_num,
        'end': end_line
    })
    print(f"  {section_id}: 行{line_num+1}-{end_line+1}")

# 目标顺序
target_order = ['background', 'cases', 'corpus', 'analytics', 'features', 'design', 'roadmap']

# 提取section代码
section_codes = {}
for s in sections:
    section_codes[s['id']] = '\n'.join(lines[s['start']:s['end']+1])

# 重建
header = '\n'.join(lines[:sections[0]['start']])
footer = '\n'.join(lines[sections[-1]['end']+1:])

# 按目标顺序拼接
new_parts = [header]
for section_id in target_order:
    if section_id in section_codes:
        new_parts.append(section_codes[section_id])

new_parts.append(footer)
new_content = '\n'.join(new_parts)

# 写回
with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

# 验证
print("\n最终顺序:")
for i, section_id in enumerate(target_order, 1):
    print(f"  {i}. {section_id}")

# 验证JS语法
import subprocess
result = subprocess.run(['node', '--check', '/workspace/projects/assets/index-D9h_BwJ2.js'], 
                       capture_output=True, text=True)
if result.returncode == 0:
    print("\n✅ JS语法检查通过!")
else:
    print(f"\n❌ JS语法错误: {result.stderr[:200]}")

print("\n完成!")
