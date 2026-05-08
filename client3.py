import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 6000))

while True:
    msg = input()
    s.send(msg.encode())
    if msg == "exit":
        break
    reply = s.recv(1024).decode()
    print("Server says:", reply)

s.close()