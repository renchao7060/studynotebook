'''
1、*args,**kwargs使用

*和**的语法.用*args和**kwargs只是为了方便并没有强制使用它们.
当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数.
*args和**kwargs可以同时在函数的定义中,但是*args必须在**kwargs前面.
当调用函数时你也可以用*和**语法.例如:
'''

def print_three_things(a,b,c):
    print('a={0},b={1},c={2}'.format(a,b,c))
	
mylist=['aard','baboon','cat']
print_three_things(*mylist)

def print_everything(*args):
    for count,thing in enumerate(args):
	    print('{}.{}'.format(count,thing))
		
print_everything('apple','banana','cabbage')

def table_thing(**kwargs):
    for name ,value in kwargs.items():
	    print('{0}={1}'.format(name,value))
		
table_thing(apple='fruit',cabbage='vagetable')


'''
2、如何获取实例的类名
'''

import itertools

x=itertools.count(0)
print(x.__class__.__name__)

print(type(x).__name__)

print(type(5).__name__)
print((5).__class__.__name__)

# count
# count
# int
# int

'''
3、python中用什么代替switch语句
我想写一个函数,实现输入一个值对应输出另一个值.
'''

def f(x):
    return {'a':1,'b':2}[x]
	
print(f('a'))

def f(x):
    return {'a':1,'b':2}.get(x,9)  # 9 is default if x not found
	
print(f('a'))
print(f('c'))

'''
4、生成包含大写字母和数字的随机字符串
'''

import string
import random

def id_generator(size=6,chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
	
print(id_generator())


'''
5、如何在一个表达式里合并两个字典?
'''

x={'a':1,'b':2}
y={'b':10,'c':11}

z1=dict(list(x.items())+list(y.items()))
print(z1)

from collections import Counter
z2=dict(Counter(x)+Counter(y))
print(z2)

# {'a': 1, 'b': 10, 'c': 11}
# {'a': 1, 'b': 12, 'c': 11}




