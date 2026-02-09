import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))   # IP, Port
server.listen(1)

print("Server waiting for connection...")
conn, addr = server.accept()
print("Connected with", addr)

conn.send(b"Hello Client")
conn.close()
