#-*- coding:utf-8 -*-

import socket,os

server=socket.socket()
server.bind(('localhost',9000))
server.listen()

while True:
    client,addr=server.accept()
    while True:
        cmd_req=client.recv(1024)
        print(cmd_req.decode('utf-8'))
        if not cmd_req:#not 0 即为True,只有为True时候才会触发下面的打印信息
            print('The client hsa losted')
            break
            
        cmd_rep=os.popen(cmd_req.decode('utf-8')).read()#接收字符串，执行结果也是字符串，因此需转码发给客户端
        if len(cmd_rep)==0:
            print('The commend is wrong')
        
        client.send(str(len(cmd_rep.encode('utf-8'))).encode('utf-8'))
        '''#计算返回报文长度切记将字符串转为字节码再len计算大小，因为字节码是字符3倍大小
        先发送报文大小给客户端，客户端根据报文大小使用While判断进行多次接收，
        直到接收的报文与报文实际大小相等退出循环'''
        
        ack_client=client.recv(1024)#等待客户端确认，确认之前一直停留在此，这样避免粘包情况出现。
        print(ack_client.decode())
        '''为了避免连续send发送出现粘包情况，在两次send之间设计一次recv，等待客户端回应后再send.
        time.sleep(0.5)也是一种方式，不过效率较低'''
        
        client.send(cmd_rep.encode('utf-8'))
server.close()