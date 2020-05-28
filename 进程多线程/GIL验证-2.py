import threading
import datetime

def calc():
    sum=0
    for i in range(200000000):
        sum+=1
    print(sum)

start=datetime.datetime.now()
tasks=[]
for i in range(4):
    t=threading.Thread(target=calc)
    tasks.append(t)
    t.start()

for t in tasks:
    t.join()

stop=datetime.datetime.now()
time=(stop-start).total_seconds()
print(time)

'''
200000000
200000000
200000000
200000000
38.928082
'''

'''
计算密集型使用多线程因为涉及线程间不断调度，所以使用的时间反而比串行的方式时间稍微长一些。
GIL只允许解释器进程中的一个线程进入CPU进行计算，这里虽然启用4个线程，但因为GIL的存在导致
只有一个线程进入CPU，所以在计算密集型情况下多线程意义不大。
'''