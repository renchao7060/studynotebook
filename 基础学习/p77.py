
from threading import Thread
from multiprocessing import Process
import time

def countdown(n):
	while n>0:
		n-=1
count=100000000
		
def thread_process_job(n,Thread_Process,job):
	start=time.time()
	thread_or_process=[Thread_Process(target=job,args=(count/n,)) for i in range(n)]
	for i in thread_or_process:
		i.start()
	for i in thread_or_process:
		i.join()
	print(n,Thread_Process.__name__,"run job need",time.time()-start)

if __name__=='__main__':
	print('Multi Threads')
	for i in [1,2,4]:
		thread_process_job(i,Thread,countdown)
	print('Multi Process')
	for i in [1,2,4]:
		thread_process_job(i,Process,countdown)