import socket
import threading

# Create a socket to connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))  # Replace with server IP and port

# Function to send messages
def send_messages():
    print("Me: ")
    while True:
        print("---------------------------------------------------")
        message = input()
        client_socket.send(message.encode())
        print("---------------------------------------------------")
        
        # print("--->")

# Function to receive and display messages
def receive_messages():
    print("Receive messages from server broadcast")
    while True:
        print("---------------------------------------------------")        
        message = client_socket.recv(1024).decode()
        print("Received: ", message)
        print("---------------------------------------------------")


# Create separate threads for sending and receiving messages
send_thread = threading.Thread(target=send_messages)
receive_thread = threading.Thread(target=receive_messages)

send_thread.start()
receive_thread.start()