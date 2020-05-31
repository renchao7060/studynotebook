'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，
故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波那契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 3，n ∈ N*）
通过多种编码实现，了解函数、递归、生成器概念及应用。
下面使用Python编程通过基本函数处理、递归思想、生成器构建等方式去解决当前问题。
方式一使用递归思想实现，思路简单直接，但随计算量的增加耗费机器资源较大。
方式二、三、四使用基本函数实现，同样在计算很大的输入参数时候，同⼀时间将所有计算出来的⼤量结果集分配到内存当中，特别是结果集⾥还包含循环，将会耗尽机器所有资源。
方式五因使用生成器只在需要的时候调用资源到内存中，所以资源消耗很少。
'''
def fib1(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>=3:
        return fib1(n-1)+fib1(n-2)

def fib21(n):
    count,a,b=1,1,1
    while count <=n:
        print(a)
        a,b=b,a+b
        count+=1

def fib22(n):
    a,b=1,1
    results=[]
    for i in range(n):
        results.append(a)
        a,b=b,a+b
    return results

def fib23(n):
    result=[1,1]
    if 1<=n<=2:
        return result
    if n>=3: 
        for i in range(n-2):
            data=result[-1]+result[-2]
            result.append(data)
        return result
        
def fib3(n):
    a,b=1,1
    for i in range(n):
        yield a
        a,b=b,a+b
    
if __name__=='__main__':
    print('方式一'.center(50,'*'))
    print(type(fib1(12)))#<class 'int'>
    print(fib1(12))

    print('方式二'.center(50,'*'))
    # fib21(5).__class__.__name__ 
    fib21(6)


    print('方式三'.center(50,'*'))
    print(type(fib22(6)))#<class 'list'>
    for i in fib22(6):
        print(i)

    print('方式四'.center(50,'*'))
    print(type(fib23(6)))#<class 'list'>
    for i in fib23(6):
        print(i)

    print('方式五'.center(50,'*'))
    print(type(fib3(24))) #<class 'generator'>
    for i in fib3(24):
        print(i)

