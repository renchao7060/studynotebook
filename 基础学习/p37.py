#-*- coding: utf-8 -*-

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',9100))
while True:
    msg=input('>>:')
    if len(msg)==0:continue
    client.send(msg.encode('utf-8'))
    data=client.recv(1024)
    print(data.decode('utf-8'))
client.close()
