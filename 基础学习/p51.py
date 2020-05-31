
import threading
import time
from functools import reduce

# begin=time.time()
# def test_01(n):
    # sum=0
    # for i in range(1,n):
        # sum+=i
    # time.sleep(2)
    # print(sum)
    
# def test_02(n):
    # product=1
    # for i in range(1,n):
        # product*=i
    # time.sleep(3)
    # print(product)
    
# test_01(100000)
# test_02(100000)
# end=time.time()

# duration=end-begin
# print(duration)

'''方式一:直接调用--N个任务可设计N个线程各自同时跑'''  
# t1=threading.Thread(target=test_01,args=(1000,))
# t2=threading.Thread(target=test_02,args=(100,))
# t2.setDaemon(True)#主进程结束等待t1执行完毕后直接关闭进程（t2作为守护进程随着主线程结束而结束）
# t1.start()
# t2.start()
# t1.join()
# t2.join()#等待t2执行完毕后再执行主线程

# end=time.time()       
# duration=end-begin
# print(duration)

'''方式二:继承类--一个任务可设计多个线程同时跑'''

class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num
        self.sum=0
        self.product=1
    # def run(self):
        # for i in range(self.num):
            # self.sum+=i
        # print(self.sum)
    def test_01(self):
        for i in range(1,self.num):
            self.sum+=i
        time.sleep(2)
        print(self.sum)
        
    def test_02(self):
        for i in range(1,self.num):
            self.product*=i
        time.sleep(3)
        print(self.product)
    def run(self):
        self.test_01()
        self.test_02()
    
t1=MyThread(100)
t2=MyThread(10)
t1.start()
t2.start()
# t1.test_01()
# t2.test_02()
