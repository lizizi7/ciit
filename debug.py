#!/usr/bin/env python3
"""使用正则表达式精确提取sections - 调试版本"""

import re

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到第一个section的完整范围
pattern = r'o\.jsx\("section", \{'
matches = list(re.finditer(pattern, content))

print(f"找到 {len(matches)} 个sections")

# 提取第一个section来测试
first_match = matches[0]
start_pos = first_match.start()

# 向前查找 section 的 id
id_pattern = r'id: "([^"]+)"'
id_match = re.search(id_pattern, content[start_pos:start_pos+500])
section_id = id_match.group(1) if id_match else "unknown"
print(f"\n测试 section: {section_id}")
print(f"  开始位置: {start_pos}")

# 找到结束位置
depth = 0
started = False
end_pos = start_pos

for j in range(start_pos, min(start_pos + 20000, len(content))):
    char = content[j]
    if char == '{':
        depth += 1
        started = True
    elif char == '}':
        depth -= 1
        if started and depth == 0:
            # 找到结束 - content[j] 是 }
            end_pos = j + 1
            print(f"  结束位置: {end_pos}")
            print(f"  结束字符: '{content[j-3:j+3]}'")
            break

section_code = content[start_pos:end_pos]
print(f"  section长度: {len(section_code)}")
print(f"  section最后20字符: {repr(section_code[-20:])}")

# 检查是否是 }) 结尾
if section_code.endswith('})'):
    print("  OK: 以 }) 结尾")
else:
    print("  ERROR: 不以 }) 结尾")
    # 看看最后是什么
    print(f"  实际结尾: {repr(section_code[-10:])}")
