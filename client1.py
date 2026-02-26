import socket

HOST = 'localhost'
PORT = 5005

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message = input("You: ")
    client.send(message.encode())

    if message.lower() == "stop":
        break

    data = client.recv(1024).decode()
    print("Server:", data)

client.close()