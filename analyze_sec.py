#!/usr/bin/env python3
"""分析section结构"""

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.readlines()

# 找到所有section
sections = []
for i, line in enumerate(lines):
    if 'o.jsx("section"' in line:
        sections.append(i)
        print(f"Section at line {i+1}: {line.strip()[:80]}")

print(f"\nTotal sections: {len(sections)}")

# 检查每个section应该在哪结束
# section: o.jsx("section", { ... children: o.jsxs("div", {...}) })
# children: [ ... ] - 数组
# div结束: }
# div调用结束: )
# section对象结束: }
# section调用结束: )

# 检查每个section区域最后的几行
for sec_line in sections:
    print(f"\n=== Section at line {sec_line+1} ===")
    # 往前找200行左右的内容
    end_area = min(sec_line + 300, len(lines))
    for i in range(end_area - 10, end_area):
        print(f"{i+1}: {lines[i].rstrip()}")
