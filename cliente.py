import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Servidor: {data.decode()}")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    try:
        while True:
            message = input("Cliente: ")
            client_socket.sendall(message.encode())
    except KeyboardInterrupt:
        print("Encerrando conexão...")

    client_socket.close()

if __name__ == "__main__":
    start_client()
