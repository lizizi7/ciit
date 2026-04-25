#!/usr/bin/env python3
"""精确修复JS文件的语法错误"""

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    content = f.read()

# 问题1: Ty函数中return语句后缺少 )
# 找到 }, []), 后跟空行和 } 的地方
old_ty = '''      return (d.current && i.observe(d.current), () => i.disconnect());
    }, []),
    
}
T0.createRoot'''

new_ty = '''      return (d.current && i.observe(d.current), () => i.disconnect());
    }, []),
  );
}
T0.createRoot'''

content = content.replace(old_ty, new_ty)

# 问题2: section结束后多余的 );
# 找到 }), 后跟空行和 );
old_section = '''        ],
      }),
    })
  );
}
const my = ['''

new_section = '''        ],
      }),
    })
}
const my = ['''

content = content.replace(old_section, new_section)

# 问题3: Ty函数缺少o.jsxs return内容前的 )
# 在 }), 后添加 )
old_ty2 = '''    })
}
const zy = ['''

new_ty2 = '''    })
  )}
const zy = ['''

content = content.replace(old_ty2, new_ty2)

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'w') as f:
    f.write(content)

print("修复完成")
