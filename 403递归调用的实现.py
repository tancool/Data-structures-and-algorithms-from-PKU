
# 报错RecursionError. => Python中的递归深度限制

import sys
print(sys.getrecursionlimit()) # 此方法可以查看递归深度.默认是1000
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit()) # 此方法可以查看递归深度
# python运行过慢 => vscode 点击右键