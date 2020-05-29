
# import threading
import datetime
import multiprocessing

def calc():
    sum=0
    for i in range(200000000):
        sum+=1
    print(sum)

start=datetime.datetime.now()
if __name__=="__main__":
    tasks=[]
    for i in range(3):#四个工作进程，一个主进程
        # t=threading.Thread(target=calc)
        t=multiprocessing.Process(target=calc)
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
12.000911
'''

'''
多进程的情况下可以绕过GIL全局解释器锁，这里实现是一个主进程，4个子进程，GIL限制主进程，但4个子进程可以正常运行计算。
进程与进程间犹如国家与国家间的关系，相互关联不大。
线程与线程间共享进程的资源，线程分配的资源对于线程本身是独享的。
'''