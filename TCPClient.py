import socket

def create_client_socket():
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return client_socket
    except socket.error as err:
        print(f"Socket creation failed with error {err}")
        return None

def connect_to_server(client_socket, host, port):
    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to {host} on port {port}")
    except socket.error as err:
        print(f"Failed to connect to {host} on port {port}: {err}")
        return False
    return True

def receive_message(client_socket):
    try:
        # Receive data from the server
        message = client_socket.recv(1024)
        return message.decode('utf-8')  # Use UTF-8 for better compatibility
    except socket.error as err:
        print(f"Failed to receive message: {err}")
        return None

def main():
    # Ask the user for the host and port to connect to
    host = input("Enter the server IP address (or hostname): ") or socket.gethostname()
    port = input("Enter the server port: ")
    port = int(port) if port.isdigit() else 444  # Default to port 444 if no valid input

    # Create the client socket
    client_socket = create_client_socket()
    if not client_socket:
        return

    # Connect to the server
    if not connect_to_server(client_socket, host, port):
        return

    # Receive the message from the server
    message = receive_message(client_socket)
    if message:
        print("Message from server:", message)
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
