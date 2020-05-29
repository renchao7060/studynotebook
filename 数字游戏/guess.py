import random

guess=random.randint(1,10)
count=0
while count<3:
    count+=1
    try:
        data=int(input("Please input the data(eg:1-10):"))
    except:
        print('The data is invalid')
        continue
    if data > guess:
        print("The data is bigger")
    elif data < guess:
        print("The data is smaller")
    else:
        print("Good,you are right")
        break
    print('\n')
