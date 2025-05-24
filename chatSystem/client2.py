import socket, threading

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect(("localhost", 9999))


nickname_client2 = input("Enter your nickname:")
client2.send(nickname_client2.encode('utf-8'))

def receive_messages(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "quit":
                break
            else:
                print(msg)
        except:
            break

threading.Thread(target=receive_messages,args = (client2,),  daemon = True).start()

while True:
    msg = input()
    if msg.lower() == "quit":
        client2.send("quit".encode('utf-8'))
        client2.close()
        break
    full_msg = f"{nickname_client2}: {msg}"
    client2.send(full_msg.encode('utf-8'))