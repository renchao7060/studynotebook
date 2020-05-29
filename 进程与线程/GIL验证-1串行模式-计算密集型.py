import threading
import datetime

def calc():
    sum=0
    for i in range(200000000):
        sum+=1
    print(sum)

start=datetime.datetime.now()

calc()
calc()
calc()
calc()

stop=datetime.datetime.now()
time=(stop-start).total_seconds()
print(time)

'''
200000000
200000000
200000000
200000000
35.973573
'''