#-*- coding:utf-8 -*-

import socket,os

client=socket.socket()
client.connect(('localhost',9000))

while True:
    cmd_req=input('>>:')
    if len(cmd_req)==0:continue
    
    client.send(cmd_req.encode('utf-8'))
    
    full_data_size=client.recv(1024)
    print(full_data_size.decode('utf-8'))
    
    client.send('准备开始接收数据'.encode())
    
    receive_size=0
    receive_data=b''
    while receive_size!=int(full_data_size.decode('utf-8')):
        partdata=client.recv(1024)
        receive_size+=len(partdata)
        receive_data+=partdata
    else:#while … else 在循环条件为 false 时执行 else 语句块
        if receive_size==0:
            print('The commend is wrong')
        else:
            print('The cmd_rep size is %s'%receive_size)
            print(receive_data.decode('utf-8'))
    

client.close()
