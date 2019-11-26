import socket
import threading
import psutil
import time
connector=True
def Monitor():
    try:
        soc = socket.socket()
    except:
        print('Server creation is Failed')
    print('Successful Server creation.')
    port = 5004
    soc.bind(('', port))
    soc.listen(5)
    c, addr = soc.accept()
    print('server connected to %s' % str(addr))
    while(True):
        x,y=psutil.cpu_percent(interval=0.005, percpu=False),psutil.virtual_memory()[2]
        time.sleep(1)
        c.send((str(x) +' '+ str(y)).encode())
        if x>100 or y>100:
            global connector
            connector =False
            break
    c.close()
    soc.close()
t=threading.Thread(target=Monitor,name='Thread1',args=())
t.start()
try:
    s=socket.socket()
except:
    print('Server creation is Failed' )
print('Successful Server creation.')
port=5003
s.bind(('',port))
s.listen(5)
c,addr=s.accept()
print('server connected to %s'% str(addr))
file = open('Data.txt', 'w+')
file.write(c.recv(1024).decode())
file.close()
file = open('Data.txt', 'a+')
while(connector):
    file.write(c.recv(1024).decode())
    file.write('\n')
# c.send(file.read().encode())
file.close()
c.close()
s.close()
