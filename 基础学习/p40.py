#-*- coding: utf-8 -*-

#python2�ļ�����
import sys
print(sys.getdefaultencoding())#ascii

s='hello,���'
print(type(s))#str

print(s)#hello,���                                                       Ĭ��Ϊ�ֽ���,gb2312��ʽ
print(s.decode('gb2312'))#hello,���                                      unicode��ʽ
print(s.decode('gb2312').encode('utf-8'))# hello,你好                   utf-8��ʽ       
print(s.decode('gb2312').encode('utf-8').decode('utf-8'))#hello,���      unicode��ʽ

# print(s.encode('utf-8'))

# print(s.encode('utf-8').decode('utf-8'))

# print(s.encode('gbk'))

# print(s.encode('gbk').decode('gbk'))


# print(s.decode('utf-8'))