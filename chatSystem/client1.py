import socket, threading

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(("localhost", 9999))


nickname_client1 = input("Enter your nickname:")
client1.send(nickname_client1.encode('utf-8'))

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

threading.Thread(target=receive_messages, args = (client1,),  daemon = True).start()

while True:
    msg = input()
    if msg.lower() == "quit":
        client1.send("quit".encode('utf-8'))
        client1.close()
        break
    full_msg = f"{nickname_client1}: {msg}"
    client1.send(full_msg.encode('utf-8'))
