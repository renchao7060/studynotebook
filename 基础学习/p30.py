# 两种继承方式 super(subclass,self).__init__(*args/**kwargs)   B.__init__(self,*args/**kwargs)


#_*_coding=UTF-8_*_

class Person(object):
    def __init__(self,mouth,foot):
        self.mouth=mouth
        self.foot=foot
        
    def talk(self):
        print('Humans has %s mouth and have the ability to speak'%self.mouth)

    def move(self):
        print('Humans have %s feet and have the ability to walk'%self.foot)

class Wisdom(object):
    def __init__(self,brain):
        self.__brain=brain
        self.friends=[]
    def think(self):
        print('Humans have %s brain and have the ability to think'%self.__brain)
    def diff(self,obj):
        print('The main difference between %s and %s is skin color'%(self.name,obj.name))#Yellow\Black类被实例化调用后生成self.name
        self.friends.append(obj)

    
    
class Yellow(Person,Wisdom):
    def __init__(self, mouth, foot, brain, color, name):
        # 采用super()方式时，会自动找到第一个多继承中的第一个父类，
        # 但是如果还想强制调用其他父类的init()函数或两个父类的同名函数时，就要用老办法了。
        super(Yellow, self).__init__(mouth,foot)#方法一
        Wisdom.__init__(self,brain)
        self.color=color
        self.name=name
        
    def yellow(self):
        print('%s is a %s face'%(self.name,self.color))
        
class Black(Person,Wisdom):
    def __init__(self,mouth,foot,brain,color,name):
        Person.__init__(self,mouth,foot)#方法二
        Wisdom.__init__(self,brain)
        self.color=color
        self.name=name
        
    def black(self):
        print('%s is a %s face'%(self.name,self.color))
        

p1=Yellow(1,2,1,'yellow','jim')
p1.talk()
p1.move()
p1.think()
p1.yellow()


p2=Black(1,2,1,'black','john')
p2.talk()
p2.move()
p2.think()
p2.black()
p3=Black(1,2,1,'black','zhen')
p3.name='chao'
p1.diff(p2)
p1.diff(p3)

print(p1.friends[0].name)