# -*- coding: utf-8 -*-

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('开始连接服务端')
client.connect(('localhost',8100))
print('开始向服务端发送数据')
client.send('你好服务端，我是客户端'.encode('utf-8'))
print('开始接收服务端数据')
data=client.recv(1024)
print(data.decode('utf-8'))
print('开始关闭客户端连接')
client.close()
print('客户端连接关闭')