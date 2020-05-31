'''
执行至主程序的末尾时,解释器会自动退出. 但是如果需要中途退出程序, 你可以调用sys.exit 函数, 
它带有一个可选的整数参数返回给调用它的程序. 这意味着你可以在主程序中捕获对sys.exit 的调用。
（注：0是正常退出，其他为不正常，可抛异常事件供捕获!）
'''
#coding:utf-8

import sys

def exitfunc(value):
    '''Clear function'''
    print (value)
    sys.exit(0)
 
print ("hello")
 
try:
    sys.exit(1)
except SystemExit as value:
    exitfunc(value)
 
print ("come?")