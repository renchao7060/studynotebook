#使用字典实现switch语句

#coding:utf-8

# def jia(x,y):
	# return(x+y)
# def jian(x,y):
	# return(x-y)
# def cheng(x,y):
	# return(x*y)
# def chu(x,y):
	# return(x/y)
	
# def operate(x,o,y):
	# if o=='+':
		# print(jia(x,y))
	# elif o=='-':
		# print(jian(x,y))
	# elif o=='*':
		# print(cheng(x,y))
	# elif o=='/':
		# print(chu(x,y))
	# else:
		# pass
# operate(3,'+',4)

# dict1={'+':jia,'-':jian,'*':cheng,'/':chu}

# def operate(x,o,y):
	# print(dict1.get(o)(x,y))
	
# operate(4,'+',2)
# operate(4,'-',2)
# operate(4,'*',2)
# operate(4,'/',2)
	

class Compute(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def compute(self,obj):
		print(obj.compute())

class Jia(Compute):
	def compute(self):
		return(self.x+self.y)
		
class Jian(Compute):
	def compute(self):
		return(self.x-self.y)

class Cheng(Compute):
	def compute(self):
		return(self.x*self.y)

class Chu(Compute):
	def compute(self):
		return(self.x/self.y)

c1=Compute(4,2)

t1=Jia(4,2)
t2=Jian(4,2)
t3=Cheng(4,2)
t4=Chu(4,2)

# t1.compute()
# t2.compute()
# t3.compute()
# t4.compute()
c1.compute(t1)
c1.compute(t2)
c1.compute(t3)
c1.compute(t4)

