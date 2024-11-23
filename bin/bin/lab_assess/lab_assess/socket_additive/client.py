import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345

client_socket.connect((host, port))

try:
    message = client_socket.recv(1024).decode()
    print(f"Message from server: {message}")

    while True:
        user_input = input("Enter a message to send to the server: ")

        client_socket.send(user_input.encode())

        response = client_socket.recv(1024).decode()
        print(f"Response from server: {response}")

except KeyboardInterrupt:
    print("\nClient is shutting down...")

finally:
    client_socket.close()
    print("Connection closed.")
