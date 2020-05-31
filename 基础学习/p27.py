
import threading

def thread_job():
    print('This is a thread of %s' % threading.current_thread())

def thread_job2():
    print('This is a thread of %s'% threading.current_thread())

def main():
    thread = threading.Thread(target=thread_job2,)   # 定义线程 threading.Thread()接收参数target代表这个线程要完成的任务，需自行定义
    thread.start()  # 让线程开始工作
    
if __name__ == '__main__':
    main()