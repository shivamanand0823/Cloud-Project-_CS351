import socket
import threading
connector=True
def Monitor():
    try:
        soc1 = socket.socket()
    except:
        print('Failed Client Socket creation!')
    print('Successful Client socket creation.')
    port1 = 5002
    soc1.connect(('127.0.0.1', port1))
    while(True):
        x=soc1.recv(1024).decode()
        print(x)
        a,b=x.split(' ')
        print(a,b)
        if float(a)>=75 or float(b)>=100:
            global connector
            connector=False
            break
    c.close()
    soc1.close()
def Monitors():
    try:
        soc2 = socket.socket()
    except:
        print('Failed Client Socket creation!')
    print('Successful Client socket creation.')
    port1 = 5004
    soc2.connect(('127.0.0.1', port1))
    while(True):
        x=soc2.recv(1024).decode()
        print(x)
        a,b=x.split(' ')
        print(a,b)
        if float(a)>100 or float(b)>100:
            global connector
            connector=False
            break
    c.close()
    soc2.close()
try:
    s=socket.socket()
except:
    print('Server creation is Failed' )
print('Successful Server creation.')
port=5000
s.bind(('',port))
s.listen(5)
c,addr=s.accept()
print('server connected to %s'% str(addr))
Username1='Varun'
Username2='Shivam'
Username3='Rushikesh'
Password='Cloud'
string=c.recv(1024).decode()
x,y=string.split(' ')
if((x== Username1 or x==Username2 or x==Username3) and y==Password):
    c.send(('Login Successful'+' '+x).encode())
    try:
        soc = socket.socket()
    except:
        print('Failed Client Socket creation!')
    print('Successful Client socket creation.')
    port1 = 5001
    soc.connect(('127.0.0.1', port1))
    t = threading.Thread(target=Monitor, name='Thread1', args=())
    t.start()
    while(connector):
        try:
            soc.send(c.recv(1024).decode().encode())
        except:
            break
    print('close')
    data=''
    l = soc.recv(1024).decode()
    while (l):
        data = data + l
        l = soc.recv(1024).decode()
    soc.close()
    try:
        soc = socket.socket()
    except:
        print('Failed Client Socket creation!')
    print('Successful Client socket creation.')
    port1 = 5003
    soc.connect(('127.0.0.1', port1))
    t = threading.Thread(target=Monitors, name='Thread1', args=())
    t.start()
    # print(data)
    soc.send(data.encode())
    while (True):
        try:
            soc.send(c.recv(1024).decode().encode())
        except:
            pass
            # print('m')
else:
    c.send('Login Unsuccessful Please Try Again'.encode())
    # soc.close()
c.close()
s.close()