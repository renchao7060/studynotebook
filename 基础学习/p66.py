
from random import randint

chinese=[randint(60,100) for _ in range(40)]
math   =[randint(60,100) for _ in range(40)]
english=[randint(60,100) for _ in range(40)]

# for i in range(len(math)):
    # sum=chinese[i] + math[i] +english[i]
    # print(sum)

total=[]    
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)
print(total)

#########################################################

from itertools import chain

e1=[randint(60,100) for _ in range(40)]
e2=[randint(60,100) for _ in range(41)]
e3=[randint(60,100) for _ in range(42)]
e4=[randint(60,100) for _ in range(39)]

count=0
for i in chain(e1,e2,e3,e4):
    if i>90:
        count+=1
print(count)