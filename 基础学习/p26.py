#_*_coding:UTF-8_*_

# 形参 def test(x,y)
# 实参test(1,2)

# 位置参数def test(x,y)
# 关键字参数 def test(x,y=1) or test(x,y=1)
# 默认参数 def test(x,y=1)
# 可选参数 def (x,y,*args,**kwargs)

def test1():
	print('in the test1')
	
def test2():
	print('in the test2')
	return 0
x=test1()
y=test2()
print(x,y)
print('*'*60)

# in the test1
# in the test2
# None 0

def test3(x,y):
	print(x,y)

test3(1,2)
test3(2,1)
test3(x=1,y=2)
test3(y=2,x=1)
test3(1,y=2)
#test3(y=2,1)#SyntaxError: positional argument follows keyword argument#关键值参数一定要放在位置参数之后
print('*'*60)

# def test4(x=1,y):#关键值参数一定要放在位置参数之后
	# print(x,y)

def test5(x,y=2):##默认参数
	print(x,y)
test5(2)#调用的时候针对默认参数可以不添加
test5(2,3)
test5(x=2)
print('*'*60)

def test6(x,y,*args,**kwargs):#可选参数*args接收位置参数以元组形式输出，*kwargs接收关键字参数以字典的方式输出
	print(x,y,args,kwargs)
	
test6(1,2)
test6(1,2,3,4,5)
test6(1,2,3,4,5,name='renchao',gender='M',age=30)
test6(1,2,name='renchao',gender='M',age=30)
test6(1,2,**{'name':'renchao','gender':'M','age':30})
print('*'*60)

# 1 2 () {}
# 1 2 (3, 4, 5) {}
# 1 2 (3, 4, 5) {'name': 'renchao', 'age': 30, 'gender': 'M'}
# 1 2 () {'name': 'renchao', 'age': 30, 'gender': 'M'}
# 1 2 () {'name': 'renchao', 'age': 30, 'gender': 'M'}

name='renchao'#全局变量
def test7():
	name='zhenzhen'#局部变量
	print(name)#zhenzhen
	# name='zhenzhen'
	# print(name)

test7()
print(name)#renchao
print('*'*60)


name='A'#全局变量为字符串或是数字的时候不建议使用此种方式进行修改
def test8():
	global name#指定在函数内部调用全局变量
	name='B'#在函数内部修改全局变量
	print(name)#B

test8()
print(name)#B
print('*'*60)




def test8():
	global name#指定在函数内部调用全局变量，而全局变量未在全局显是建立，这种方法杜绝使用
	name='B'#在函数内部修改全局变量
	print(name)#B

test8()
print(name)#B
print('*'*60)


#通过函数可修改全局变量为字典，列表，集合等数据
dict1={'name':'renchao','gender':'man'}
list1=[1,2,3,4,5]
set1={1,2,3,5}

def test9():
	print(dict1['name'])#renchao
	print(list1[0])#1
	print(set1.pop())#1
	dict1['name']='zhenzhen'
	list1[0]=10
	set1.add(10)
	print(dict1)
	print(list1)
	print(set1)
	

test9()
print(dict1)
print(list1)
print(set1)

# renchao
# 1
# 1
# {'name': 'zhenzhen', 'gender': 'man'}
# [10, 2, 3, 4, 5]
# {10, 2, 3, 5}
# {'name': 'zhenzhen', 'gender': 'man'}
# [10, 2, 3, 4, 5]
# {10, 2, 3, 5}


# 局部变量是字符串或是数字形式的，修改局部变量不能自动改全局变量
# 局部变量是字典，集合，列表形式的，修改局部变量能自动改全局变量





