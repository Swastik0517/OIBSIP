import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5

clients = []  

def handle_client(client, address):
    print(f"[NEW CONNECTION] {address} connected.")
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Client {address}: {message}")
            reply = input("You: ")
            client.send(reply.encode("utf-8"))
        except:
            print(f"[DISCONNECTED] {address}")
            clients.remove(client)
            client.close()
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"SERVER RUNNING on {HOST}:{PORT}")
    except:
        print(f"Unable to bind to Host {HOST} and Port {PORT}")
        return

    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        clients.append(client)
        print(f"[CONNECTED] {address[0]}:{address[1]}")
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()

if __name__ == '__main__':
    main()
