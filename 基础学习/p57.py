'''
from multiprocessing import Process,Queue

def f(q):
    q.put([1,2,3])
    
if __name__=='__main__':
    q=Queue()
    p1=Process(target=f,args=(q,))
    p1.start()
    print(q.get())
    p1.join()
'''   
from multiprocessing import Process,Pipe

def child(conn):
    conn.send('hello')
    conn.close()
    
if __name__=='__main__':
    parent_conn,child_conn=Pipe()
    p1=Process(target=child,args=(child_conn,))
    p1.start()
    print(parent_conn.recv())
    p1.join()