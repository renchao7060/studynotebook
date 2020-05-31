#_*_coding:UTF-8_*_

class Game():
	area='china'#类变量，各实例共用的属性，节省内存开销
	def __init__(self,name,role,weapon,life_value=10,money=1000):#构造函数
		self.name=name#实例变量（静态属性），实例变量的优先级高于类变量
		self.role=role
		self.weapon=weapon
		self.__life_value=life_value
		self.__money=money
		
	def get_role(self):#类方法（动态属性）
		print('%s is %s'%(self.name,self.role))
		
	def get_gun(self):
		print('%s spend 10$ on a %s'%(self.name,self.weapon))
		self.__money-=10
		
	def get_shoot(self):
		print('%s was shot,his life value minus 10'%self.name)
		self.__life_value-=10
		
	def show_status(self):
		print('%s life_value:%s,money:%s'%(self.name,self.__life_value,self.__money))
		
	def __del__(self):#析构函数，默认程序执行完毕自动调用
		print('game over\n')
		

player1=Game('jim','police','AK47')
player1.get_role()
player1.get_gun()
player1.get_shoot()
player1.show_status()
del player1


player2=Game('john','terrorist','AK90')
player2.get_role()
player2.get_gun()
player2.get_shoot()
player2.show_status()

