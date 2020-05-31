# 列表是线程不安全的

import threading
import time

list1=[1,2,3,4,5]

def pri():
    while list1:
        a=list1[-1]
        print(a)
        time.sleep(2)
        try:
            list1.remove(a)
            # del list1[-1]
        except:
            print('----',a)
t1=threading.Thread(target=pri)
t1.start()
t2=threading.Thread(target=pri)
t2.start() 
'''
5
5
4
---- 5
4
3
---- 4
3
2
---- 3
2
1
---- 2
1
---- 1
'''