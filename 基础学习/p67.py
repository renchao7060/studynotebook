#阶乘计算，计算1+2！+3！...+10!的结果
sum,tmp=0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print('运算结果是：{}'.format(sum))

#猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。
#第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
#到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''
这题得倒着推。第10天还没吃，就剩1个，说明第9天吃完一半再吃1个还剩1个，假设第9天还没吃之前有桃子p个，
可得：p * 1/2 - 1 = 1，可得 p = 4。以此类推，即可手算出。
代码思路为：第10天还没吃之前的桃子数量初始化 p = 1，之后从9至1循环9次，根据上述公式反推为 p = (p+1) * 2 
可得第1天还没吃之前的桃子数量。for循环中的print()语句是为了验证推算过程而增加的。代码如下：
'''
# p=1
# for i in range(9,0,-1):
    # p=(p+1)<<1
    # p=(p+1)*2
    # print('第%s天吃之前还有%s个桃子' % (i, p))
# print('第1天共摘了%s个桃子' % p)


#健康食谱输出 列出5种不同的食材，请输出他们可能组成的所有菜式名称

# diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
# count=0
# for x in range(0,5):
    # for y in range(0,5):
        # if not (x==y):
            # print('{}{}'.format(diet[x],diet[y]))
            # count+=1
# print('共组合食谱数量为{}'.format(count))


#五角星的绘制

# from turtle import *
# fillcolor('red')
# begin_fill()
# while True:
    # forward(200)
    # right(144)
    # if abs(pos())<1:
        # break
# end_fill()


#太阳花的绘制

# from turtle import *
# color('red','yellow')
# begin_fill()
# while True:
    # forward(200)
    # left(170)
    # if abs(pos())<1:
        # break
# end_fill()
# done()

#螺旋线绘制

# import turtle
# import time

# turtle.speed('fastest')
# turtle.pensize(2)
# for x in range(100):
    # turtle.forward(2*x)
    # turtle.left(90)
# time.sleep(3)


#彩色螺旋线的绘制

# import turtle
# import time

# turtle.pensize(2)
# turtle.bgcolor('black')
# colors=['red','green','yellow','blue']

# turtle.tracer(False)

# for x in range(400):
    # turtle.forward(2*x)
    # turtle.color(colors[x%4])
    # turtle.left(91)
# turtle.tracer(True)
# turtle.done()


#############
# for i in range(5):
    # print("*"*(i+1))



