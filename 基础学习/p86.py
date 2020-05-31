from toolkit.managers import Timer
from threading import Thread
from multiprocessing import Process

class Thread_Process(Process):
	def __init__(self,n):
		Process.__init__(self)
		self.n=n

	def test_thread_process(self,n):
		while self.n>0:
			self.n-=1

	def run(self):
		self.test_thread_process(self.n)



if __name__=='__main__':
	with Timer() as timer:
		count=100000000
		n=4
		tps=[Thread_Process(count/n) for _ in range(n) ]
		for t in tps:
			t.start()
		for t in tps:
			t.join()
	print(timer.cost)






# if __name__=='__main__':
# 	# t=Thread(target=test_thread_process,args=(100000000,))
# 	# t.start()
# 	# t.join()
# 	# p=Process(target=test_thread_process,args=(100000000,))
# 	# p.start()
# 	# p.join()
# 	with Timer() as timer:
# 		t1=Process(target=test_thread_process,args=(100000000/4,))
# 		t2=Process(target=test_thread_process,args=(100000000/4,))
# 		t3=Process(target=test_thread_process,args=(100000000/4,))
# 		t4=Process(target=test_thread_process,args=(100000000/4,))

# 		t1.start()
# 		t2.start()
# 		t3.start()
# 		t4.start()

# 		t1.join()
# 		t2.join()
# 		t3.join()
# 		t4.join()
# 	print(timer.cost)



