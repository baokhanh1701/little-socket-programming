import socket
import threading

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))  # Use a specific IP and port
server_socket.listen(5)

# List to hold connected clients
clients = []

# Function to broadcast messages to all connected clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                print(client, "sended: ", message)
                client.send(message)
            except:
                # Remove the client if the connection is no longer valid
                clients.remove(client)
                print("Client exited")

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break

# Accept and handle incoming connections
while True:
    print(f"Connecting...")
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Connection from {client_address}")
    print(f"Receiving from connection...")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()