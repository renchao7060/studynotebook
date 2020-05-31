# 进程间共享数据-Manager
from multiprocessing import Process,Manager

def f(d,l,i):
    d[1]=1
    d[2]=2
    d[3]=3
    d['a']=4
    l.append(i)
    print(l)
    print()
    
if __name__=='__main__':
    with Manager() as manger:
        d=manger.dict()
        l=manger.list(range(5))
        p_list=[]
        for i in range(10):
            p=Process(target=f,args=(d,l,i))
            p.start()
            p_list.append(p)
        
        for p in p_list:
            p.join()
        print(d)
        print(l)