

from multiprocessing import Process
import os

def test1(title):
    print(title)
    print('moudul name',__name__)
    print('parent process',os.getppid())
    print('child process',os.getpid())
    print('\n\n')

def test2(name):
    test1('\033[31;1msub process\033[0m')
    print('subprocess',name)
    
if __name__=='__main__':
    test1('\033[32;1mmain process\033[0m')
    p=Process(target=test2,args=('chao',))
    p.start()
    p.join()
    print('main process:hello zhen')