import datetime
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def calc():
    sum=0
    for i in range(200000000):
        sum+=1
    print(sum)

start=datetime.datetime.now()
if __name__=="__main__":
    excutor=ThreadPoolExecutor(4)
    with excutor:
        for i in range(4):
            excutor.submit(calc)

    stop=datetime.datetime.now()
    time=(stop-start).total_seconds()
    print(time)

'''

200000000
200000000
200000000
200000000
39.22811

'''
