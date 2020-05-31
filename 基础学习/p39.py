#-*- coding: utf-8 -*-

#python2文件编码
import sys
print(sys.getdefaultencoding())#ascii

# s=u'hello,你好'
# print(type(s))#unicode

# print(s)#unicode格式                                  hello,你好
# print(s.encode('utf-8'))#utf-8格式                    hello,浣犲ソ##为何utf-8为乱码
# print(s.encode('utf-8').decode('utf-8'))#unicode格式  hello,你好
# print(s.encode('gbk'))#gbk格式                        hello,你好
# print(s.encode('gbk').decode('gbk'))#unicode格式      hello,你好




# s1='hello,你好'  #utf-8格式（默认与文本输出工具编码一致），为二进制字节码

# print(s1)#hello,浣犲ソ                                            utf-8格式
# print(s1.decode('utf-8'))#hello,你好                              unicode格式
# print(s1.decode('utf-8').encode('utf-8'))#hello,浣犲ソ            utf-8格式
# print(s1.decode('utf-8').encode('gbk'))#hello,你好                gbk格式


# print(s1.decode('gbk'))#hello,浣犲ソ
# print(s1.decode('gbk').encode('utf-8'))#hello,娴ｇ姴銈

# pycharm与notepad执行结果不一致，应该和文本编辑器编码有关


s2=b'hello,你好'   二进制字节码  utf-8编码

print(s2)#hello,浣犲ソ
print(s2.decode('utf-8'))#hello,你好
