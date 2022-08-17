import socket

from header_creator import header_creator

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),6969))
while True:
    try:
        t = input("Msg: ")
        header = header_creator("01",t)
        s.send(header)
        s.send(bytes(t,"utf-8"))
    except KeyboardInterrupt:
        s.send(header_creator(" C",""))
        s.close()
        break
