#coding:utf-8

import os
import pickle
os.chdir('E:\Progect')


info={'name':'renchao','age':31,'weight':65,'height':155}

pic1=pickle.dumps(info)
print(type(pic1),pic1)

dict1=pickle.loads(pic1)
print(type(dict1),dict1)

# <class 'bytes'> b'\x80\x03}q\x00(X\x06\x00\x00\x00weightq\x01KAX\x04\x00\x00\x00nameq\x02X\x07\x00\x00\x00renchaoq\x03X\x03\x00\x00\x00ageq\x04K\x1fX\x06\x00\x00\x00heightq\x05K\x9bu.'
# <class 'dict'> {'weight': 65, 'name': 'renchao', 'age': 31, 'height': 155}


with open('pick1.text','wb') as f:
	pickle.dump(info,f)
	
with  open('pick1.text','rb') as f:
	data=pickle.load(f)
	print(data['name'])#renchao