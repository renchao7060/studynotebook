# -*- coding: utf-8 -*-

import socket
import os

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9100))
server.listen(3)
while True:
    client,addr=server.accept()
    while True:
        try:
            data=client.recv(1024)
            print(data.decode())
            # if not data:
                # print('client has lost...')
                # break
            client.send(b"I'm server")
        except ConnectionResetError as e:
            print('The client%s has dicconnected,info%s'%(addr,e))
            break
        except ConnectionAbortedError as e:
            print('The client%s use ctr+c quit,info%s'%(addr,e))
            break
            # msg=os.system(data.decode())
            # print(type(msg))
            # client.send(str(msg).encode('utf-8'))
            # msg=os.popen(data).read()
            # client.send(msg)
server.close()
