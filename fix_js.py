#!/usr/bin/env python3
# Find and fix the two issues

with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'r') as f:
    lines = f.read().split('\n')

# Issue 1: Fix the line with "}, []),\n\n}\n" pattern (Ty function)
# This should be "}, []),\n  )\n}"
for i in range(len(lines)):
    if lines[i].strip() == '}, []),':
        # Check if next line is empty or }
        if i+1 < len(lines) and lines[i+1].strip() == '}':
            print(f"Found Ty function pattern at line {i+1}")
            print(f"Line {i+1}: {lines[i]}")
            print(f"Line {i+2}: {lines[i+1]}")
            lines[i+1] = '  )' + '\n' + '}'
            print(f"After fix:")
            print(f"Line {i+1}: {lines[i+1]}")
            break

# Issue 2: Fix the line "  });" that should be just "}"
# Find the section end pattern "    })\n  );\n}\n"
for i in range(len(lines)):
    if lines[i].strip() == '    })' and i+1 < len(lines) and lines[i+1].strip() == '  );' and i+2 < len(lines) and lines[i+2].strip() == '}':
        if 'const my' in lines[i+3]:
            print(f"\nFound section end pattern at line {i+1}")
            print(f"Line {i+1}: {lines[i]}")
            print(f"Line {i+2}: {lines[i+1]}")
            print(f"Line {i+3}: {lines[i+3]}")
            # Remove lines[i+1] and lines[i+2] (the ); and })
            lines.pop(i+1)  # Remove );
            lines.pop(i+1)  # Remove }
            print(f"After fix, section ends at line {i+1}")
            break

# Write back
with open('/workspace/projects/assets/index-D9h_BwJ2.js', 'w') as f:
    f.write('\n'.join(lines))

print("\nFile updated!")
