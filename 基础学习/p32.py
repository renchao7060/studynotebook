#多态，同一接口不同输出
# 当子类和父类都存在相同的bulk()方法时，子类的bulk()覆盖了父类的bulk()，在代码运行时，会调用子类的 bulk()
# 这样，我们就获得了继承的另一个好处：多态。 
# 多态的好处就是，当我们需要传入更多的子类，例如新增 Tiger、Pig 等时，我们只需要继承 Animal 类型就可以了，
# 而bulk()方法既可以不重写（即使用Animal的），也可以重写一个特有的。这就是多态的意思。
# 调用方只管调用，不管细节，而当我们新增一种子类时，只要确保新方法编写正确，而不用管原来的代码。这就是著名的“开闭”原则：
# 对扩展开放（Open for extension）：允许子类重写方法函数
# 对修改封闭（Closed for modification）：不重写，直接继承父类方法函数
	
	
#coding:utf-8

class Animal(object):
	print('继承父类特性')
	def bulk(self,obj):#将子类实例化名字传入
		obj.bulk()
	# def bulk(self):
		# print('Animal is bulking')
	
class Dog(Animal):
	def bulk(self):
		print('Dog is bulking wang wang')
	

class Cat(Animal):
	def bulk(self):
		print('Cat is bulkingmiao miao')
		
d1=Dog()
# d1.bulk()

c1=Cat()
# c1.bulk()

A1=Animal()
A1.bulk(d1)
A1.bulk(c1)

print(isinstance(d1,Dog))
print(isinstance(d1,Animal))
print(issubclass(Dog,Animal))
# print(issubclass(d1,A1))#issubclass() arg 1 must be a class