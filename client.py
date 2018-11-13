from check import usercheck
import os
import socket
import threading
def login():
    usertel=input("请输入手机号:")
    #发送验证码
    u=usercheck()
    upass1=u.Check(usertel)
    print(upass1)
    upass2=input("请输入您收到的验证码:")
    if upass1==upass2:
        path=r"D:\liaotianshi\zhanghu"
        tellist=[tel[:-4] for tel in os.listdir(path)]
        #如果登陆过，则获取到对方昵称，继续下一步
        name=None
        if usertel in tellist:
            file=open(path+"\\"+usertel+".txt","r+")
            name=file.read()
            file.close()
            print("欢迎回来，%s"%(name))
        #如果没登陆过，则让对方输入昵称，继续下一步
        else:
            name=input("请输入您的昵称:")
            file=open(path+"\\"+usertel+".txt","w+")
            file.write(name)
            file.close()
        #下一步:连接服务器，创建socket，将昵称发送过去，选择聊天室，并且启动两个线程
        return name

    else:
        print("验证码不正确")
        login()

def csend(s):
    while True:
        str=input().encode("utf-8")
        s.send(str)

def crecv(s):
    while True:
        print(s.recv(1024).decode("utf-8"))



if __name__=="__main__":
    print("欢迎使用chatroom")
    name=login()
    s=socket.socket()
    s.connect(("192.168.10.139",8887))
    s.send(name.encode("utf-8"))
    index=input("请选择聊天室：1，动漫世界    2，英雄联盟   3，数码科技    4，悄悄话")
    s.send(index.encode("utf-8"))

    threading.Thread(target=csend,args=(s,)).start()
    threading.Thread(target=crecv,args=(s,)).start()

