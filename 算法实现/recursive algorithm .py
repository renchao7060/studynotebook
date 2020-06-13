'''
recursive algorithm   /rɪˈkɜːrsɪv/  /ˈælɡərɪðəm/     递归算法
Recursive Formulation /rɪˈkɜːrsɪv/  /ˌfɔːrmjuˈleɪʃn/ 递归算法
arithmetic  /əˈrɪθmətɪk/ 算法
algorithm implementation /ˈælɡərɪðəm/  /ˌɪmplɪmenˈteɪʃn/ 算法实现
'''
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
#     digui(2)
#         digui(1)
#             digui(0)
#             =========
#             print(0)
#         print(1)
#     print(2)
# print(3)

def digui2(num,count):
    print('*'*num)
    if num <count:
        digui2(num+2,count)
    print('*'*(num-2))

digui2(1,9)








# 汉诺塔戏
def move1(n,a,b,c):
    if n==1:
        print(a,'-->',c)
        return
    move1(n-1,a,c,b)
    move1(1,a,b,c)
    move1(n-1,b,a,c)
# move1(3,'a','b','c')

print('分隔线'.center(20,'-'))
def move2(n,src,dst,tmp=None):
    if n==1:
        print(src,'-->',dst)
        return
    move2(n-1,src,tmp,dst)
    move2(1,src,dst)
    move2(n-1,tmp,dst,src)
# move2(3,'a','c','b')
print('分隔线'.center(20,'-'))
def move3(n,src='a',tmp='b',dst='c'):
    if n==1:
        print(src,'-->',dst)
        return
    move3(n-1,src,dst,tmp)
    move3(1,src,tmp,dst)
    move3(n-1,tmp,src,dst)
# move3(3)