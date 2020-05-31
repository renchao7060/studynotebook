

import threading,time,random,queue

q=queue.Queue()

def producer(name):
    count=0
    while count<5:
        time.sleep(random.randrange(3))
        q.put(count)
        print('%s生产了%s个包子'%(name,count))
        count+=1
        
def concumer(name):
    count=0
    while count<5:
        time.sleep(random.randrange(4))
        if not q.empty():
            q.get()
            print('%s吃了%s个包子'%(name,count))
        else:
            print('没有包子')
        count+=1
        
        
t1=threading.Thread(target=producer,args=('A',))
t1.start()
t2=threading.Thread(target=concumer,args=('B',))
t2.start()
            
