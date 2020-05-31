#如何对迭代器做切片处理
#文本文件可适用
from itertools import islice

# list1=range(20)
# t=iter(list1)

# for i in islice(t,5,10,2):
    # print(i)
    
    
import os
print(os.getcwd())

f=open('langs.model.xml','r')
for line in islice(f,10,11):
    print(line)
    
# for line in f:
    # print(line)