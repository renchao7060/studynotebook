
import threading,time,random,queue

class Producter(threading.Thread):
    def run(self):
        while True:
            r=random.randint(1,100)
            q.put(r)
            print('生产出来%s号包子'%r)
            time.sleep(3)

class Consumer(threading.Thread):
    def run(self):
        while True:
            re=q.get()
            print('吃掉%s号包子'%re)
            
if __name__=='__main__':
    q=queue.Queue(3)
    threads=[]
    for i in range(3):
        threads.append(Producter())
    threads.append(Consumer())
    # print(threads)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    