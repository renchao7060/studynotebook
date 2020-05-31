#python3文件编码
import sys
print(sys.getdefaultencoding())#utf-8

s='hello,你好'
print(type(s))
print(s)#hello,你好 unicode格式

print(s.encode('utf-8'))#b'hello,\xe4\xbd\xa0\xe5\xa5\xbd'  utf-8格式（3字节标识一汉字） 汉字以二进制字节码bytes显示

print(s.encode('utf-8').decode('utf-8'))#hello,你好         unicode格式

print(s.encode('gbk'))#b'hello,\xc4\xe3\xba\xc3'            gbk格式(2字节标识一汉字)，汉字以以二进制字节码bytes显示

print(s.encode('gbk').decode('gbk'))#hello,你好             unicode格式


print(s.decode('utf-8'))#AttributeError: 'str' object has no attribute 'decode'  unicode格式没有decode方法，说明s默认格式是unicode

