import socket
import threading

# Function to handle each client connection
def handle_client(client_socket, addr):
    print(f"New connection from {addr}")
    
    # Send welcome message to the client
    client_socket.send(b"Connection established. Please send your message!")
    
    while True:
        try:
            # Receive message from client
            data = client_socket.recv(1024).decode()
            if not data:  # If no data is received, the client has disconnected
                print(f"Client {addr} disconnected.")
                break
            print(f"Received from {addr}: {data}")
            
            # Server sends message back to the client
            response = input(f"Enter response for {addr}: ")
            client_socket.send(response.encode())
        
        except ConnectionResetError:
            print(f"Client {addr} forcefully disconnected.")
            break

    client_socket.close()


# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and port
host = '127.0.0.1'
port = 12345

# Bind the socket to the port
server_socket.bind((host, port))

# Start listening for connections (max 5 clients can queue)
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

try:
    while True:
        # Accept new connection
        client_socket, addr = server_socket.accept()
        
        # Create a new thread for each client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

except KeyboardInterrupt:
    print("\nServer is shutting down...")

finally:
    # Close the server socket
    server_socket.close()
    print("Server closed.")
