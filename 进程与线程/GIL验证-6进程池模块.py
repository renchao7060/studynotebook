import datetime
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def calc():
    sum=0
    for i in range(200000000):
        sum+=1
    print(sum)

start=datetime.datetime.now()
if __name__=="__main__":
    excutor=ProcessPoolExecutor(4)
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
13.101967

'''

'''
总结
# 串行35s
#多线程38s 多线程上下文切换应该多一点点相时,对于CPU密集型代码来说,Python的多线程由于GIL所以没有任何优势
#多进程12s 真并行,绕过了GIL,GIL解释器锁
#进程池实现4个进程12s
#ThreadPoolExecutor 39s
#ProcessPoolExecutor 13s

'''