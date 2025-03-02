import socket

def main():
    # This print is just for debugging logs:
    print("Logs from your program will appear here!")

    # Create a TCP server on port 9092.
    # By default, 'socket.create_server()' will:
    #   - create a socket
    #   - bind it to the given host/port
    #   - set it to listen mode
    #
    # reuse_port=True allows you to re-run without "port already in use" errors 
    # (depending on your environment).
    server_socket = socket.create_server(("0.0.0.0", 9092), reuse_port=True)

    # Block until a client connects (the tester will connect to this port).
    server_socket.accept()

if __name__ == "__main__":
    main()