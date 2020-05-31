#装饰器是对闭包功能的使用

#_*_coding:UTF-8_*_

def dec(func):
  def in_func(*arg):
    print('2:in_func arg is',arg)
    if len(arg)==0:
      return 0
    for val in arg:
      if not isinstance(val,int):
        return 0
    return func(*arg)
  print('1:in dec')
  return in_func
  
  
@dec#等价于my_sum=dec(my_sum)
def my_sum(*arg):
  print('3:in my_sum')
  return sum(arg)
def my_average(*arg):
  print('in my_average')
  return sum(arg)/len(arg)
  
print(my_sum(1,2,3,4))
# 打印结果：
# 1:in dec
# 2:in_func arg is (1, 2, 3, 4)
# 3:in my_sum
# 10
#=========================================================================================================================
#装饰器-传入的函数不带参数
def decorator(func):
  def in_func():
    print('2:in_func')
    return func()
  print('1:in decorator')
  return in_func

@decorator#等价于car=decorator(car)  
def car():
  print('3:in car')
  print('The car is very good')
  print('\n\n')
  
car()
# 输出结果：
# 1:in decorator
# 2:in_func
# 3:in car
# The car is very good

#=========================================================================================================================
#装饰器-传入的函数带参数

def deco(func):
  def in_func(age,weight,*arg):
    print("The boy's height is",arg[0])
    return func(age,weight,*arg)
  return in_func

@deco#等价于man=deco(man) 
def man(age,weight,*arg):
  print("The boy's age is",age)
  print("The boy's weight is",weight)
  
man(10,'30k','150cm')

# 输出结果：
# The boy's height is 150cm
# The boy's age is 10
# The boy's weight is 30k

