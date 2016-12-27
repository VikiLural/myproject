import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
size = 1024
s.bind(("localhost", 8000))
s.listen(1)
con, add = s.accept()

while True:
    req = con.recv(size).decode('UTF-8')
    splt = req.split(' ')
    f = open(splt[1], 'rb')
    answ = f.read()
    con.send(answ)
con.close
s.close()