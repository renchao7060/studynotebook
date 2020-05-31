#-*- coding: utf-8 -*-

#python2文件编码
import sys
print(sys.getdefaultencoding())#ascii

s='hello,你好'
print(type(s))#str

print(s)#hello,你好                                                       默认为字节码,gb2312格式
print(s.decode('gb2312'))#hello,你好                                      unicode格式
print(s.decode('gb2312').encode('utf-8'))# hello,浣犲ソ                   utf-8格式       
print(s.decode('gb2312').encode('utf-8').decode('utf-8'))#hello,你好      unicode格式

# print(s.encode('utf-8'))

# print(s.encode('utf-8').decode('utf-8'))

# print(s.encode('gbk'))

# print(s.encode('gbk').decode('gbk'))


# print(s.decode('utf-8'))