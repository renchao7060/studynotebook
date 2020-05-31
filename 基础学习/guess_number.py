import random

choice=random.randint(1,10)
while True:
    guess=int(input('please input your number:'))
    if guess==choice:
        print('You are right')
        break
    elif guess>choice:
        print('guess bigger')
        continue
    else:
        print('guess smaller')
        continue
