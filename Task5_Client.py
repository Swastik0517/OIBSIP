import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"\nServer: {message}") 
        except:
            print("\n[DISCONNECTED] Server closed the connection.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print("Connected to server.")
    except:
        print("Connection failed.")
        return

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        message = input("You: ")
        if message.lower() == "quit":
            client.close()
            break
        client.send(message.encode("utf-8"))

if __name__ == '__main__':
    main()
