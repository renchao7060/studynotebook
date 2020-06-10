'''
Python获取当前脚本绝对路径
此处分享在python下获取一个脚本的绝对路径的2种方式。
1、__file__变量

abs_file=__file__
print("abs path is %s" %(__file__))
abs_dir=abs_file[:abs_file.rfind("\\")]     # windows下用\\分隔路径，linux下用/分隔路径

简单直接，当前py文件的绝对目录就有了。首推此方式。
2、os+sys

import os
import sys
print("abs path is %s" %(os.path.abspath(sys.argv[0])))

在windows下sys.argv[0]直接取出的就是参数，如果执行命令传参用的是绝对路径取出的就是带绝对路径，
如果传参用的是相对路径，就用得上前面的os.path.abspath()函数了。

'''
import random
import os
import sys
# abs_path=__file__
# root=os.path.abspath(__file__)
# root=os.path.abspath(sys.argv[0])
# print(root)
# dad=os.path.dirname(__file__)
os.chdir(os.path.dirname(__file__))

print(os.getcwd())

for i in range(160):
    data=random.randint(20,50)
    # print(data)
    data=str(data)
    with open('data.txt','a') as f:
        f.write(data)
        f.write('\n')