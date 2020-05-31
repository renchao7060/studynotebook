#-*-coding:utf-8 -*-

import random

rand=random.randint(1,10)
count=0

# while count<3:
    # guess=int(input('>>:'))
    # if guess==rand:
        # print('you are right')
        # break
    # elif guess > rand:
        # print('guess bigger')
    # else:
        # print('guess smaller')
    # count+=1
# else:#以上循环结束后执行此else内容
    # print('you guess too many times')
        
        
        
# while count<3:
    # guess=int(input('>>:'))
    # if guess==rand:
        # print('you are right')
        # break
    # elif guess > rand:
        # print('guess bigger')
    # else:
        # print('guess smaller')
    # count+=1
    # if count==3:#这个思路挺好
        # answer=input('do you guess again?')
        # if answer!='n':
            # count=0
  




for count in range(3):#for 循环使用
    guess=int(input('>>:'))
    if guess==rand:
        print('you are right')
        break
    elif guess > rand:
        print('guess bigger')
    else:
        print('guess smaller')
    count+=1
else:
    print('you guess too many times')

            