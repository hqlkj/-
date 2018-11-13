import socket
import threading
list=[[],[],[],[]]


def run(s,name,index):
    while True:
        #一旦收到这个线程发出的任何消息，
        # 就给出了这个线程之外的所有线程发送
        str=s.recv(1024).decode("utf-8")
        print(str)
        for ss in list[index]:
            if ss!=s:
                ss.send((name+":"+str).encode("utf-8"))

if __name__=="__main__":
    server=socket.socket()
    server.bind(("192.168.10.139",8887))
    server.listen(50)
    while True:
        s,addrs=server.accept()
        name=s.recv(1024).decode("utf-8")
        index=int(s.recv(1024).decode("utf-8"))-1
        list[index].append(s)
        threading.Thread(target=run,args=(s,name,index,)).start()
