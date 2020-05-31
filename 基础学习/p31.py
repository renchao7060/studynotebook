#各类之间实例化后，通过实例化名字在各类之间进行调用

#coding:utf-8

class School(object):
	def __init__(self,name,addr):
		self.name=name
		self.addr=addr
		self.enrool_students=[]#注意在构造函数内部定义新的变量需要self.开头（这里的变量可在类实例化时不必传参数）
		self.hire_teachers=[]
		
	def enroll(self,stu_obj):
		print('%s 正在注册学籍'%stu_obj.name)
		self.enrool_students.append(stu_obj)
		
	def hire(self,tea_obj):
		print('%s被%s雇佣'%(tea_obj.name,self.name))
		self.hire_teachers.append(tea_obj)

		
class SchoolMember(object):
	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex
		
	def tell():
		pass
		
class Teacher(SchoolMember):
	def __init__(self,name,age,sex,salary,course):
		super(Teacher,self).__init__(name,age,sex)
		self.salary=salary
		self.course=course
	def tell(self):
		print('''
		-------------Teacher.info:%s-----------
		name:%s
		age:%s
		sex:%s
		salary:%s
		course:%s
		'''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
	def teach(self):
		print('%s is teaching %s'%(self.name,self.course))
		
class Student(SchoolMember):
	def __init__(self,name ,age,sex,stu_id,grade):
		super(Student,self).__init__(name,age,sex)
		self.stu_id=stu_id
		self.grade=grade
	def tell(self):
		print('''
		---------------Student.info:%s-----------
		name:%s
		age:%s
		sex:%s
		stu_id:%s
		grade:%s
		'''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))
	def pay_tuition(self,amount):
		print('%s need to pay tution  %s '%(self.name,amount))

school=School('济南分校','槐荫区')

t1=Teacher('jim',31,'M',10000,'python')#实例化后可在其它类中进行调用，如School中enrool方法传入t1实例
t2=Teacher('john',32,'M',10000,'linux')
t1.tell()
# t1.teach()

s1=Student('yanning',15,'M',10001,1)#实例化后可在其它类中进行调用，如School中hire方法传入s1实例
s2=Student('zhenzhen',20,'F',20001,6)
s1.tell()
# s1.pay_tuition(500)

school.enroll(s1)
school.enroll(s2)
# print(school.enrool_students)#列表中为s1,s2实例名
school.enrool_students[0].pay_tuition(200)
school.enrool_students[0].pay_tuition(1000)
print('*'*60)

school.hire(t1)
school.hire(t2)
# print(school.hire_teachers)#列表中为t1,t2实例名
school.hire_teachers[0].teach()
school.hire_teachers[1].teach()