
import datetime
import multiprocessing

def calc():
    sum=0
    for i in range(200000000):
        sum+=1
    print(sum)

start=datetime.datetime.now()
if __name__=="__main__":
    pool=multiprocessing.Pool(4)
    
    for i in range(4):#四个工作进程，一个主进程
        pool.apply_async(calc)

    pool.close()
    pool.join()
    

    stop=datetime.datetime.now()
    time=(stop-start).total_seconds()
    print(time)

'''

200000000
200000000
200000000
200000000
12.010845

'''
'''
多进程的情况下可以绕过GIL全局解释器锁，这里实现是一个主进程，4个子进程，GIL限制主进程，但4个子进程可以正常运行计算。
进程与进程间犹如国家与国家间的关系，相互关联不大。
线程与线程间共享进程的资源，线程分配的资源对于线程本身是独享的。
'''