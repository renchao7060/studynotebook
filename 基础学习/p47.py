import socket
import hashlib
import os

# print(os.getcwd())
os.chdir('E:\\Progect\\Practice_9.19\\practice\\tmp')



server=socket.socket()
server.bind(('localhost',9999))
server.listen(5)

while True:
    conn,addr=server.accept()
    while True:
        data=conn.recv(1024)
        if not data:
            break
        cmd,filename=data.decode().split()
        if os.path.isfile(filename):
            f=open(filename,'rb')
            m=hashlib.md5()
            file_size=os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                conn.send(line)
                m.update(line)
            print('flie md5',m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())
        print('send done')
server.close()