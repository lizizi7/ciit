#!/usr/bin/env python3
"""分析第一个section的结束"""

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# 第一个section开始
sec_start = 15354  # 0-indexed

# 往前找section的children: [
# o.jsx("section", { ... children: o.jsxs("div", { ... children: [ ... ] }) })

# 找到section的children（div）
print("From section start:")
for i in range(sec_start, sec_start + 20):
    print(f"{i+1}: {lines[i].rstrip()[:80]}")

# 找到div的children数组开始
div_children_start = None
for i in range(sec_start, sec_start + 50):
    if 'children: [' in lines[i]:
        div_children_start = i
        print(f"\nDiv children array starts at line {i+1}")
        break

# 从div children数组开始，找到匹配的 ] 结束
# 这应该就是section的结束

# 计算到下一个section
print("\n\nLooking for section end before next section (line 15557):")
for i in range(15550, 15560):
    print(f"{i+1}: {lines[i].rstrip()[:80]}")
