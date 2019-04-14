import socket
words={'how are you?':'Fine,thank you.','how old are you?':'38','what is your name?':'KuroNeko','what is your name?':'KuroNeko','where do you work?':'SDIBT','bye':'Bye'}

HOST=''
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
print('Listening at port:',PORT)
conn,addr=s.accept()
print('Connected by',addr)
while True:
    data=conn.recv(1024)#接收
    data=data.decode()#转码
    if not data:
        break
    print('Received message:',data)
    conn.sendall(words.get(data,'Nothing').encode())#返回字典中键为data的值，若不存在返回'Nothing'
conn.close()
s.close()