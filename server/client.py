import socket
import threading


HEADER = 64 # İLETİLEBİLECEK METİN KARAKTER SINIRI
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE =  "!DISCONNECT"
SERVER = "192.168.1.33"
ADDR = (SERVER , PORT)



client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_legth = str(msg_length).encode(FORMAT)
    send_legth += b" " * (HEADER - len(send_legth))
    client.send(send_legth)
    client.send(message)


    print(client.recv(2048).decode(FORMAT))


print(client.recv(2048).decode(FORMAT))


while True:

    message = input("> ")
    
    if message == "/stop":
        send(DISCONNECT_MESSAGE)
        break
    else:
        send(message)
    
        
    
    



