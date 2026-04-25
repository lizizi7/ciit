#!/usr/bin/env python3
import re

with open('assets/index-D9h_BwJ2.js', 'r') as f:
    content = f.read()

# 找到所有section的开始位置
section_starts = [m.start() for m in re.finditer(r'o\.jsx\("section",\s*\{', content)]
print(f"找到 {len(section_starts)} 个sections")

# 手动提取每个section的范围（使用括号匹配）
sections = []
for i, start in enumerate(section_starts):
    # 从start位置开始，找到匹配的结束
    pos = start
    brace_count = 0
    in_section = False
    section_start = -1
    section_end = -1
    
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
            in_section = True
            if section_start == -1:
                section_start = pos
        elif content[pos] == '}':
            brace_count -= 1
        elif content[pos] == ')' and brace_count == 1:
            # 找到 o.jsx(...) 的结束
            section_end = pos + 1
            break
        pos += 1
    
    if section_start != -1 and section_end != -1:
        sections.append(content[section_start:section_end])

print(f"提取了 {len(sections)} 个sections")

# 目标顺序: [background, cases, corpus, analytics, features, design, roadmap]
# 原始顺序: [background, corpus, analytics, features, design, roadmap, cases]
# 需要: background保持不动，cases移到第2位，其余顺序不变

# 打印原始顺序
print("\n原始顺序:")
for i, s in enumerate(sections):
    match = re.search(r'id:\s*"(.*?)"', s)
    print(f"  {i+1}. {match.group(1) if match else 'unknown'}")

# 构建新顺序
new_order = [sections[0]]  # background
new_order.append(sections[6])  # cases -> 第2位
new_order.extend(sections[1:6])  # corpus, analytics, features, design, roadmap

print("\n新顺序:")
for i, s in enumerate(new_order):
    match = re.search(r'id:\s*"(.*?)"', s)
    print(f"  {i+1}. {match.group(1) if match else 'unknown'}")

# 构建新的sections字符串
new_sections = '\n'.join(new_order)

# 找到return语句的范围
first_section_start = section_starts[0]
return_start = content.rfind('return (', 0, first_section_start)
return_end = content.find(');', first_section_start)

# 提取return之前的部分和之后的部分
before_return = content[:return_start]
return_stmt = content[return_start:return_end + 2]
after_return = content[return_end + 2:]

# 找到return语句结束后的 } 闭合函数
func_end = after_return.find('}')
after_func = after_return[func_end + 1:]

# 构建新内容
new_content = before_return + return_stmt.replace(
    content[first_section_start:return_end],
    new_sections
) + after_func

with open('assets/index-D9h_BwJ2.js', 'w') as f:
    f.write(new_content)

print("\n完成！sections已重新排列")
