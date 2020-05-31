#_*_coding:UTF-8_*_

#list1=[x for x in range(10000000000)]#列表中一次生成所有的对象，再通过for循环调用逐一查看，一次生成太多数据极易瞬间耗尽内存
#gene1=(x for x in range(10000000000))#通过for循环或是next函数调用的时候才生成对象


#通过函数实现fibonacii
# def fib(max):
  # n,a,b=0,0,1
  # while n<max:
    # print(b)
    # a,b=b,a+b
    # n+=1
  # return 'done'
    
# fib(10)
# print('*'*60)


# 通过生成器实现fibonacii
def fib(max):
  n,a,b=0,0,1
  while n<max:
    yield b
    a,b=b,a+b
    n+=1
  return 'done'
'''若通过for循环逐一调用数据的话不会打出‘done’,使用next方法调用可以，但我们无法手动依次打印N次。
此函数已是生成器而不是函数，这里的return是在程序异常时候报错信息'''

# print(fib(10))#函数体中有yield说明是生成器，通过for调用或是next调用逐一输出
#<generator object fib at 0x0000025834CDCAF0>

ge=fib(10)
while True:
  try:
    x=next(ge)
    print(x)
  except StopIteration as e:
    print(e.value)
    break
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# done #输出结果有‘done’

# print(ge.__next__())#1
# print(ge.__next__())#1
# print(ge.__next__())#2
# print(ge.__next__())#3
# print(next(ge))#5
# ......

# for i in ge:
  # print(i)#8,13,21,34,55