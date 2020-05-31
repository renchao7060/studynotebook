#-*- coding:utf-8 -*-

#静态方法实际跟类没有直接关系了，只是使用类的实例化进行调用
#类方法只能调用类变量，不能调用实例变量
#属性方法将一个类方法转化为成一个静态属性，这样就无法通过（）进行参数传递，需通过@方法名.setter单独设置
class Dog(object):
    '''类 高级方法演示'''
    name='xiaobai'#类变量
    def __init__(self,name,toy):
        self.name=name#实例变量
        self.__toy=None
    def eat(self):
        print('%s is eating'%self.name)
    @staticmethod
    def bulk(self):
        print('%s is bulking'%self.name)
    @staticmethod
    def compute():
        for i in range(1,10):
            for j in range(1,i+1):
                print('%s*%s=%s '%(j,i,j*i),end='')
            print('\n',end='')
    @classmethod
    def move(self):
        print('%s is moving'%self.name)
    @property
    def play(self):
        print('%s is playing %s'%(self.name,self.__toy))
    @play.setter
    def play(self,toy):
        self.__toy=toy
        print('set toy to:',self.__toy)
        print('%s is playing %s'%(self.name,self.__toy))
    @play.deleter
    def play(self):
        del self.__toy
        print('删除属性')
        
d=Dog('xiaohui','brick')
d.eat()
d.bulk(d)
d.move()
d.play
# d.play('train')

d.play='train'  #@play.setter 以此赋值的方式直接调用d.play
d.play

# del d.play
# d.play

d.compute()

print(Dog.__doc__)#类 高级方法演示
print(d.__module__)#__main__
print(d.__class__)#<class '__main__.Dog'>
print(Dog.__dict__)#打印类中的所有属性和方法，不包含实例中的属性
print(d.__dict__)#打印实例属性，不包含类属性  {'name': 'xiaohui', '_Dog__toy': 'train'}
# print(d.__toy)#AttributeError: 'Dog' object has no attribute '__toy'
print(d._Dog__toy)#train 隐藏属性的查看方式
      