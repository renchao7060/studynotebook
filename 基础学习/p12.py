#_*_coding:UTF-8_*_

import time

def consumer(name):
  print('%s 开始准备吃包子了'%name)
  while True:
    baozi=yield
    print('%s 正在吃%s 包子'%(name,baozi))

def producter():
  c1=consumer('A')
  c2=consumer('B')
  c1.__next__()#调用yield但是不传值
  c2.__next__()
  print('老子准备做包子了')
  for i in range(1,5):
    time.sleep(1)
    print('做好了一个包子分两半给你们')
    c1.send(i)#send 调用yield并给其传值
    c2.send(i)
	
producter()