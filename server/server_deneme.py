import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

users_r = {} # id den isime    ############################################
users = {}  # isimden id ye
conns = {}


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    ############
    conn.send("komutlar : \nkullanıcı listesi = /users\nçıkış = /stop \nadınız : ".encode(FORMAT))
    

    msg_length = conn.recv(HEADER).decode(FORMAT)
    msg_length = int(msg_length)
    msg = conn.recv(msg_length).decode(FORMAT)

    if msg in users:
        pass
    else:
        users[msg] = addr
        conns[msg] = conn
        users_r[addr] = msg  #########################################
        
    
    conn.send(" ".encode(FORMAT))  ######## "Msg received"


    for i in conns: # i  kullanıcı isimleri          kullanıcılara mesajı iletmek için

                if  conns[i] != conn:

                    conns[i].send(f"\n{msg} bağlandı".encode(FORMAT))
                    conn.send(" ".encode(FORMAT)) ######## "Msg received"
                else:
                    conn.send(" ".encode(FORMAT)) ######## "Msg received"
                    break



    connected = True
    while connected:

       
        
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        
  
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                for i in users:
                    if users[i] == addr:
                        del users[i]
                        del conns[i]
                        del users_r[addr]

                        break
                
                
                
                
            elif msg == "/users":
                print(users)
                conn.send(str(list(users.keys())).encode(FORMAT))

            for i in conns: # i  kullanıcı isimleri          kullanıcılara mesajı iletmek için

                if  conns[i] != conn:

                    conns[i].send(f"\n[{users_r[addr]}] {msg}".encode(FORMAT))
                    
                else:
                    conn.send(" ".encode(FORMAT)) ######## "Msg received"
                    break

            print(f"[{addr} {users_r[addr]}] {msg}")
 
            #conn.send("Msg received".encode(FORMAT))


    conn.close()




def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    
    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client,args=(conn, addr))
        thread.start()
        
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

        


print("[STARTING] server is starting...")

start()
    
    