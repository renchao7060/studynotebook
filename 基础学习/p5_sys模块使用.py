'''
功能：执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数，
带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对sys.exit的调用。（0是正常退出，其他为异常）
'''

import sys

def exitfunc(value):
  print(value)
  sys.exit(0)
  
print('hello')
 
try:
  sys.exit(1)
except SystemExit as value:
  exitfunc(value)

print('come?')

# hello
# 1 #come?未打印

# =================================================================================================================
'''
import sys
print('The commend line argument is ')
for i in sys.argv:
  print(i)
  
print("\n\nThe PYTHONPATH is ",sys.path,'\n')

'''
'''
E:\Progect\tmp>python3 usesys.py we are argument
The commend line argument is
usesys.py
we
are
argument


The PYTHONPATH is  ['E:\\Progect\\tmp', 'C:\\Python35\\python35.zip', 'C:\\Python35\\DLLs', 'C:\\Python35\\lib', 'C:\\Python35', 'C:\\Python35\\lib\\site-packages']
'''
# ========================================================================================================================