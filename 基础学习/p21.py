'''
shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
'''
#_*_coding:utf-8_*_

import shelve
import os
os.chdir(r'e:\progect')

name=['renchao','zhenzhen','yanning']
dict={'name':'renchao','gender':'man','weight':65}
class Test():
	def __init__(self,n):
		self.n=n
		print(n)

t1=Test(1234)
t2=Test(4567)
print(t1,t2)

d=shelve.open('test')
#写入数据,在本地生成三个文件tmp.dir tmp.dat tmp.bak
d['name']=name
d['dict']=dict
d['t1']=t1
d['t2']=t2
#读取数据
print(d.get('name'))#['renchao', 'zhenzhen', 'yanning']
print(d.get('dict'))#{'weight': 65, 'gender': 'man', 'name': 'renchao'}
print(d.get('t1'))#<__main__.Test object at 0x00000176470330F0>
print(d.get('t2'))#<__main__.Test object at 0x0000017647033860>
d.close()



