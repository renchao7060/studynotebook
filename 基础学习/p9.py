#闭包调用函数func

#_*_coding:UTF-8_*_


# def my_sum(*arg):
  # if len(arg)==0:
    # return 0
  # for val in arg:
    # if not isinstance(val,int):
      # return 0
  # return sum(arg)
  
# def my_average(*arg):
  # if len(arg)==0:
    # return 0
  # for val in arg:
    # if not isinstance(val,int):
      # return 0
  # return sum(arg)/len(arg)
  
# print(my_sum(1,2,3,4))#10
# print(my_average(1,2,3,4))#2.5
  
def my_sum(*arg):
  print('in my_sum')
  return sum(arg)
def my_average(*arg):
  print('in my_average')
  return sum(arg)/len(arg)

def dec(func):
  def in_func(*arg):
    print('in_func arg is',arg)
    if len(arg)==0:
      return 0
    for val in arg:
      if not isinstance(val,int):
        return 0
    return func(*arg)
  return in_func
  
f1=dec(my_sum)
f2=dec(my_average)
print(f1(1,2,3,4))
print(f2(1,2,3,4))

# 打印结果：
# in_func arg is (1, 2, 3, 4)
# in my_sum
# 10
# in_func arg is (1, 2, 3, 4)
# in my_average
# 2.5
  
