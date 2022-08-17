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
    connected = True
    while connected:
        header = cclient.recv(10)
        header_string = header.decode("utf-8")
        print(header_string)


        #Handles sending messages to the server
        if header_string.split("|")[0] == "01":
            msg=cclient.recv(int(header_string.split("|")[1],0))
            print(msg.decode("utf-8"))
        #Handles disconnecting server
        if header_string.split("|")[0] == " C":
            cclient.close()
            connected = False

while True:
    client, address = s.accept()
    print(address)
    threading.Thread(target=handle_client,args=(client,address)).start()
    