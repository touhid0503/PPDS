import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

msg = client.recv(1024)
print("Server says:", msg.decode())

client.close()
