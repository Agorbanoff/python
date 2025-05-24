import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(2)

print("server is running...")

client1, addr1 = server.accept()
nickname1 = client1.recv(1024).decode('utf-8')

client2, addr2 = server.accept()
nickname2 = client2.recv(1024).decode('utf-8')

client1.send(f"{nickname1} connected\n".encode('utf-8'))
client2.send(f"{nickname2} connected\n".encode('utf-8'))

def handle_client(client, other_client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "quit":
                break
            else:
                other_client.send(msg.encode('utf-8'))
        except:
            break
    client.close()
    other_client.close()

threading.Thread(target=handle_client, args=(client1, client2)).start()
threading.Thread(target=handle_client, args=(client2, client1)).start()
