'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
'''

#_*_coding:UTF-8_*_

while True:
  try:
    ti=input("Please enter today's date,eg:2018.7.20\n")
    year=int(ti.split('.')[0])
    month=int(ti.split('.')[1])
    day=int(ti.split('.')[2])
    break
  except:
    print('The date format is not available.\n')


# year=int(input('请输入年份：\n'))
# month=int(input('请输入月份：\n'))
# day=int(input('请输入日期：\n'))

p=[31,28,31,30,31,30,31,31,30,31,30,31]#平年
r=[31,29,31,30,31,30,31,31,30,31,30,31]#闰年

if year%400==0 or (year%4==0 and year%100!=0):
  dth=r
else:
  dth=p
  
sum1=sum(dth[:(month-1)])+day
print()
print('%d-%d-%d is the %dth'%(year,month,day,sum1))