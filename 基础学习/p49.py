
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data=self.request.recv(1024).strip()
                print('con add %s'%self.client_address[0])
                print('con port %s'%self.client_address[1])
                print(self.data)
                if not self.data:
                    print('client ctrl + c手动断开')
                    break
                self.request.send(self.data.upper())
            except:
                print('链接断开')
                break

if __name__=='__main__':
    host,port='localhost',9100           
    server=socketserver.ThreadingTCPServer((host,port),MyTCPHandler)
    server.serve_forever()