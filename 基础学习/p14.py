#_*_coding:UTF-8_*_

#all() 全部为真返回True
print(all([1,2,3]))#True
print(all([1,0,3]))#False

#any() 有一项为真返回True,全0或是空为False
print(any([1,2,0]))#True
print(any([]))#False

#bin() 将整数转换成二进制
print(bin(2))#0b10

# bytes()转换为字节码
a=bytes('abcde',encoding='utf-8')
print(a.capitalize(),a)#b'Abcde' b'abcde'#无法直接修改a，是针对a做了副本做的大小写操作
#字符串是不可修改的，二进制的字节格式也是不可修改的

#bytearray #可修改的二进制字节格式
b=bytearray('abcde',encoding='utf-8')
print(b)#bytearray(b'abcde')
print(b[0])#97
b[0]=98
print(b)#bytearray(b'bbcde')

#callable() #核查对象是否可调用(能加（）的一般都可被调用，如函数，类等)
print(callable([]))#False
def func():pass
print(callable(func))#True

#chr()返回数字的ascii
print(chr(97))#a
#ord()返回字母对应的ascii数值
print(ord('a'))#97



#compile(),exec() 编译字节码后执行
code='''
def func():
	print('hello word')
	
func()
'''
exec(code)#hello word
pyc=compile(code,'','exec')
exec(pyc)#hello word

#dir()#查看对象所拥有的方法
s='a'
dir(a)

#divmod()#求商取余数
divmod(5,2)#(2,1)商数为2 余数为1

#enumerate()
list1=['renchao','zhenzhen','yanning']
print(list(enumerate(list1)))
#[(0, 'renchao'), (1, 'zhenzhen'), (2, 'yanning')]

for i,v in enumerate(list1):
	print(i,v)
	
# 0 renchao
# 1 zhenzhen
# 2 yanning


#eval()#将字符串转换为其它类型进行处理
x=1
print(eval('x+1'))#2

#filter()
res=filter(lambda x:x>5,range(10))#可迭代对象
for i in res:
  print(i)
  
print(list(filter(lambda x:x>5,range(10))))#[6, 7, 8, 9]
  
  
#map()
res=map(lambda x:x**2,range(3))#可迭代对象
for i in res:
  print(i)
  
print(list(map(lambda x:x**2,range(3))))#[0,1,4]
  
  
#reduce()
from functools import reduce

res=reduce(lambda x,y:x+y,range(1,5))
print(res)#1+2+3+4=10
res=reduce(lambda x,y:x*y,range(1,5))
print(res)#1*2*3*4=24


#frozenset()#冻结集合使其不可变，正常集合set是可变的，可调用pop()\remove()\update()\union()
set1=frozenset([1,2,3,4,3,2,1])
print(set1)#frozenset({1, 2, 3, 4})

#globals() 查找本文件内所有key:value的变量
#print(globals())
#locals()查找本地变量
#hash() 求HASH值
print(hash('renchao'))

#hex()将数值转成16进制
#oct()将数值转成8进制
#id()返回对象内存地址
#input()输入信息
#int()
#isinstance('abc',str)
#iter()转化为迭代器
#len()
#max()
#min()
#next()
#sum()
#pow(2,8)2的8次方
#repr
#round(1.234,2)#1.23保留2位小数
#reversed() list(reversed(range(5)))#[4,3,2,1,0]
#type()查看数据类型
#sorted()
dict1={1:100,-1:120,10:1,7:200}
print(sorted(dict1.items()))#默认使用key排序[(-1, 120), (1, 100), (7, 200), (10, 1)]
print(sorted(dict1.items(),key=lambda x:x[1]))#调整使用value进行排序[(10, 1), (1, 100), (-1, 120), (7, 200)]
#zip
a=[1,2,3]
b=[11,12,13]
for i in zip(a,b):
	print(i)
# (1, 11)
# (2, 12)
# (3, 13)

#__import__
#map


