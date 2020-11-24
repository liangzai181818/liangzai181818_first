from socket import *      # 从类socket 中调用很多方法,用* 代替
tcp_socket=socket()
ADDR=("127.0.0.1",7777)
tcp_socket.connect(ADDR)

while True:
    data=input("请输入内容:")
    if not data:
        break
    tcp_socket.send(data.encode())
    res=tcp_socket.recv(1024)
    print(res.decode())



tcp_socket.close()









