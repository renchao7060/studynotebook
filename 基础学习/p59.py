
from multiprocessing import Process
import time

#直接调用
# def subprocess(i):
    # time.sleep(1)
    # print('hello',i)
    
# if __name__=='__main__':
    # p_list=[]
    # for i in range(300):
        # p=Process(target=subprocess,args=(i,))
        # p.start()
        # p_list.append(p)
    # for p in p_list:
        # p.join()
        
#继承父类        
class Myprocess(Process):
    def __init__(self):
        super(Myprocess,self).__init__()
    def run(self):
        time.sleep(1)
        print(self.name)
    
if __name__=='__main__':
    p_list=[]
    for i in range(10):
        p=Myprocess()
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()
        