import socket
import hashlib
import os

# print(os.getcwd())
os.chdir('E:\\Progect\\Practice_9.19\\practice\\tmp')


client=socket.socket()
client.connect(('localhost',9999))

while True:
    print('下载列表如下:\n',os.listdir(),'\n 退出：exit')
    cmd=input('下载文件格式如下：get XX\n请选择下载文件>>:').strip()
    if len(cmd)==0:
        print('输入错误')
        continue
    elif cmd=='exit':
        break
    elif cmd.startswith('get'):
        client.send(cmd.encode())
        response=client.recv(1024)
        total_file_size=int(response.decode())
        client.send(b'ready to recv')
        
        receive_size=0
        filename=cmd.split()[1]
        f=open(filename+'.down','wb')
        m=hashlib.md5()
        
        while receive_size<total_file_size:
            if total_file_size-receive_size>1024:
                size=1024
            else:
                size=total_file_size-receive_size
            
            data=client.recv(size)
            f.write(data)
            m.update(data)
            receive_size+=len(data)
        else:
            print('new file md5',m.hexdigest())
            print('receive_size:%s,total_file_size:%s'%(receive_size,total_file_size))
            f.close()
        server_file_md5=client.recv(1024)
        print('server_file_md5',server_file_md5)
        print('client_file_md5',m.hexdigest())
        print('数据下载校验完毕')
    else:
        print('命令输入错误')
client.close()
            
    
