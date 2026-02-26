import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5005))   
server.listen(1)

print("Server has been created, waiting for client...")

conn, addr = server.accept()
print("Client connected:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    print("Client:", data)

    if data.lower() == "stop":
        break

    reply = data[::-1]
    conn.send(reply.encode())

conn.close()
server.close()