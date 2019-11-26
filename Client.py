import socket
try:
    s=socket.socket()
except:
    print('Failed Client Socket creation!')
print('Successful Client socket creation.')
port=5000
s.connect(('127.0.0.1',port))
str1=input('UserName')
str2=input('Password')
str3=str1+' '+str2
s.send(str(str3).encode())
x=s.recv(1024).decode()
if(x=='Login Successful '+str1):
    print(x)
    while(True):
        data=input(str1+' >> ')
        try:
            s.send(data.encode())
        except:
            print(' Trigger process failover triggered')

print(x)
s.close()