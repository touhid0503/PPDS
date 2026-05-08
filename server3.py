import socket
import threading

client_count = 0
lock = threading.Lock()

def handle_client(conn, client_number):
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data or data == "exit":
                break
            print(f"Client {client_number} says: {data}")
            reply = input()
            conn.send(reply.encode())
    except Exception as e:
        print(e)
    finally:
        conn.close()
        print(f"Client {client_number} disconnected.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6000))
server.listen()
print("Server started. Waiting for clients...")

while True:
    conn, addr = server.accept()
    with lock:
        client_count += 1
        num = client_count
    print(f"Client {num} connected.")
    thread = threading.Thread(target=handle_client, args=(conn, num))
    thread.start()