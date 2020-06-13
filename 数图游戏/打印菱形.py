'''
# rhombus /ˈrɑːmbəs/ 菱形

   *
  ***
 *****
*******
 *****
  ***
   *
行   *数量   空格数量--->行转换为---->推算空格数量---->推算每行*数量
1    1       3         -(7//2)=-3    abs(-3)         7-2*abs(-3)=1
2    3       2         -2            abs(-2)         7-2*abs(-2)=3
3    5       1         -1            abs(-1)         7-2*abs(-1)=5
4    7       0          0            0               7-2*abs(0) =7
5    5       1          1            1               7-2*abs(1) =5
6    3       2          2            2               7-2*abs(2) =3
7    1       3          7//2         3               7-2*abs(3) =1

行起始数值 =-(7//2)    =-3
行结束数值 = (7//2)+1  = 4
每行空格值 = ' '.abs(i)         #i为当前处于哪一行
每行星号值 = '*' *(n-2*abs(i))  #n为菱形最长一行*的数量，需为奇数odd,本例中的7即为n
代码实现：
for i in range(-3,4):
    print(' '*abs(i)+'*'*(7-2*abs(i)))
'''

def rhombusg(n):
    # if not n%2:
    #     n=n+1
    start=-(n//2)
    stop=(n//2)+1
    for i in range(start,stop):
        print(' '*abs(i)+'*'*(n-2*abs(i)))

if __name__=='__main__':
    while True:
        try:
            n=int(input('Please input the odd:'))
            if n%2==1:
                rhombusg(n)
                break
            else:
                print('The input is even,it need odd')
                continue
        except:
            print('The input is invalid')
            continue