﻿#猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。
#第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
#到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''
这题得倒着推。第10天还没吃，就剩1个，说明第9天吃完一半再吃1个还剩1个，假设第9天还没吃之前有桃子p个，
可得：p * 1/2 - 1 = 1，可得 p = 4。以此类推，即可手算出。
代码思路为：第10天还没吃之前的桃子数量初始化 p = 1，之后从9至1循环9次，根据上述公式反推为 p = (p+1) * 2 
可得第1天还没吃之前的桃子数量。for循环中的print()语句是为了验证推算过程而增加的。代码如下：
'''
p=1
for i in range(9,0,-1):
    p=(p+1)<<1
    p=(p+1)*2
    print('第%s天吃之前还有%s个桃子' % (i, p))
print('第1天共摘了%s个桃子' % p)


