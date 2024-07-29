import socket
import threading

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Cliente: {data.decode()}")
        response = input("Servidor: ")
        conn.sendall(response.encode())

    conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Servidor escutando na porta 12345...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
