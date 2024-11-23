import socket

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and port to connect to the server
host = '127.0.0.1'
port = 12345

# Connect to the server
client_socket.connect((host, port))

try:
    # Receive initial message from the server
    message = client_socket.recv(1024).decode()
    print(f"Message from server: {message}")
    
    # Communication loop
    while True:
        # Get user input to send to the server
        user_input = input("Enter a message to send to the server: ")

        # Send user input to the server
        client_socket.send(user_input.encode())

        # Receive and print the server's response
        response = client_socket.recv(1024).decode()
        print(f"Response from server: {response}")

except KeyboardInterrupt:
    print("\nClient is shutting down...")

finally:
    # Close the client socket
    client_socket.close()
    print("Connection closed.")
