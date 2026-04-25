#!/usr/bin/env python3
"""修复JS文件的语法错误"""

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# 找到sections数组区域 - children: [
# 从Ty函数中的return语句中，children: [ 开始

# 首先找到Ty函数开始
ty_start = None
for i, line in enumerate(lines):
    if 'function Ty()' in line or 'function Ty ()' in line or line.strip().startswith('function Ty('):
        ty_start = i
        break

print(f"Ty function starts at line {ty_start + 1}")

# 从Ty函数开始往前找sections children: [
sections_start = None
for i in range(ty_start - 1, 0, -1):
    if 'children: [' in lines[i]:
        sections_start = i
        break

print(f"Sections children array starts at line {sections_start + 1}")

# 计算sections数组中的sections数量
section_count = 0
for i in range(sections_start, ty_start):
    if 'o.jsx("section"' in lines[i]:
        section_count += 1
        print(f"Section {section_count} starts at line {i + 1}")

# 找到sections数组结束的]
# 应该是Ty函数中的return ( ... children: [ ... ] ... )
# sections数组后应该是 ] 然后 ), 关闭children: [ 

# 找到最后一个section的位置
last_section_line = None
for i in range(len(lines) - 1, sections_start, -1):
    if 'o.jsx("section"' in lines[i]:
        last_section_line = i
        break

print(f"Last section starts at line {last_section_line + 1}")

# 从最后一个section开始，找到它的结束
# section的children是o.jsxs("div", {...})，需要找到对应的结束
# 查找 ]\s*$ 后面跟着 }), 或 }) 或类似模式

# 简化：找最后一个 ] 后跟 }), 的位置
# 这应该是sections数组结束

sections_end = None
for i in range(last_section_line, ty_start):
    stripped = lines[i].strip()
    if stripped == '],' or stripped == ']':
        # 检查下一行
        if i + 1 < ty_start:
            next_stripped = lines[i + 1].strip()
            if next_stripped == '}),' or next_stripped == '}),' or next_stripped.startswith('}),'):
                sections_end = i
                print(f"Sections array ends at line {i + 1}")
                print(f"Next line: {lines[i + 1].strip()}")
                break

# 显示sections结束区域
if sections_end:
    print("\n--- Sections end area ---")
    for i in range(max(0, sections_end - 5), min(len(lines), sections_end + 15)):
        print(f"{i+1}: {lines[i].rstrip()}")

# 检查Ty函数的return语句
print("\n--- Ty function return area ---")
return_line = None
for i in range(ty_start, min(ty_start + 20, len(lines))):
    if 'return (' in lines[i] or 'return(' in lines[i]:
        return_line = i
        print(f"Return statement at line {i + 1}")
        break

if return_line:
    for i in range(return_line, min(return_line + 15, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()}")
