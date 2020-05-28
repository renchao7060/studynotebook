import threading
import time

def worker():
    while True:
        time.sleep(1)
        print('I use {} to work'.format(threading.current_thread().name))
        time.sleep(1)

for i in range(3):
    t=threading.Thread(target=worker,name='thread{}'.format(i+1))#两个工作线程
    t.start()#一个主线程
    print('{} start,id:{}'.format(t.name, t.ident) )


'''
thread1 start,id:16928
thread2 start,id:5376
thread3 start,id:21220
I use thread1 to work
I use thread3 to work
I use thread2 to work
I use thread1 to work
I use thread3 to work
I use thread2 to work
I use thread3 to work
'''
'''
线程几种状态
就绪--调度--时间片用完--运行--等待资源--阻断
                        |
                   完成/被取消
                        |
                       终止


'''