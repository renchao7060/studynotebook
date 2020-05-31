#_*_coding:UTF-8_*_

#高阶函数-将函数以参数的形式传入或是函数return中返回函数
#递归函数-


def sums(x,y):
    print(x+y)
    return x+y

def fun(f):
    def in_fun(*args):
        print('in the in_fun')
        return f(*args)
    return in_fun

# func=fun(sums)
# print(func(1,2))


def test(n):
    print(n)
    if n-1>0:
        test(n-1)

test(996)