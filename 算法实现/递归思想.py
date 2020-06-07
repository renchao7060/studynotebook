
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(10))
# 1,1,2,3,5,8,13,21,34,55

def jiecheng(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n>1:
        return n*jiecheng(n-1)
print(jiecheng(5))

def length(lst):
    if lst[1:]:
        return 1 +length(lst[1:])
    else:
        try:
            if lst[0]:
                return 1
        except:
                return 0
print(length([1,2,3,4,5,6]))
print(length([1]))
print(length([]))

import os
count=0
def print_file(path):
    global count
    for child in os.listdir(path):
        new_path=os.path.join(path, child)
        if os.path.isdir(new_path):
            print_file(new_path)
        else:
            print(new_path)
            count+=1
        # print(count)

# currentdir=os.curdir
# print(currentdir)
# print_file('.')
# print(count)

def digui(num):
    print('$'+str(num))
    # 临界值
    if num >0:
        # 这里用的是调用本身的函数(递推关系)
        digui(num-1)
    else:
        print('='*20)
    print(num)

digui(3)