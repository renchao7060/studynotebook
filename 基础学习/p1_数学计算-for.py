'''
简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
Python解题思路分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
'''
#_*_coding:UTF-8_*_

sum=0
for i in range(1,5):
  for j in range(1,5):
    for k in range(1,5):
      if (i!=j)and(i!=k)and(j!=k):
        print(i,j,k)
        sum+=1
print(sum)