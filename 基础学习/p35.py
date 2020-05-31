# -*- coding: utf-8 -*-

import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',8100))
server.listen(5)
print('服务端开始监听')
client,addr=server.accept()
# print(client)#<socket.socket fd=348, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8100), raddr=('127.0.0.1', 20319)>
# print(addr)#('127.0.0.1', 20319)
print('开始接收客户端数据：')
data=client.recv(1024)
print(data.decode('utf-8'))
print('开始向客户端发送数据')
client.send('你好客户端，我是服务端'.encode('utf-8'))
print('关闭服务端服务')
server.close()
print('服务端已关闭')

# 服务端开始监听
# 开始接收客户端数据：
# 你好服务端，我是客户端
# 开始向客户端发送数据
# 关闭服务端服务
# 服务端已关闭