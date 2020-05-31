#_*_:coding:UTF-8_*_
#coding:utf-8
import json
import os
print(os.getcwd())#C:\Program Files\Notepad++  在此目录下无法建立文件-无权限，所以调整目录
os.chdir('E:/Progect')
print(os.getcwd())#E:\Progect

info={'name':'renchao','age':31,'weight':65,'height':155}
print(type(info),info)

js1=json.dumps(info)
print(type(js1),js1)

# <class 'dict'> {'age': 31, 'name': 'renchao', 'height': 155, 'weight': 65}
# <class 'str'> {"age": 31, "name": "renchao", "height": 155, "weight": 65}

dict1=json.loads(js1)
print(type(dict1),dict1)
# <class 'dict'> {'name': 'renchao', 'height': 155, 'age': 31, 'weight': 65}


# f=open('tmp.text','w')
# f.write(json.dumps(info))
# f.close()

#写入JSON数据--字符串
with  open('test.text','w') as f:
	json.dump(info,f)
	
#从文件中读取数据
with open('test.text','r') as f:
	data=json.load(f)
	print(data)