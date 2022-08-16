import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostbyname(socket.gethostname()),6969))
s.listen(5)
print(socket.gethostbyname(socket.gethostname())+"\n")

def handle_client(cclient: socket.socket,caddress):
    """
    Handles client requests
    """
    print("New thread")
    while True:
        header = cclient.recv(9)
        header_string = header.decode("utf-8")
        print(header_string)
        if header_string.split("|")[0] == "1":
            msg=cclient.recv(int(header_string.split("|")[1],0))
            print(msg.decode("utf-8"))
        if header_string.split("|")[0] == "C":
            break

while True:
    client, address = s.accept()
    print(address)
    threading.Thread(target=handle_client,args=(client,address)).start()
    