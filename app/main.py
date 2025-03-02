import socket
import struct

def main():
    print("Starting Kafka-like server on port 9092...")

    # Create a listening server socket on 0.0.0.0:9092
    server_socket = socket.create_server(("0.0.0.0", 9092), reuse_port=True)
    server_socket.listen()

    while True:
        conn, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # 1) Read the incoming request (we ignore its contents for this stage).
        #    We just read some bytes so the client isn't blocked.
        request_data = conn.recv(1024)
        print(f"Received request of {len(request_data)} bytes")

        # 2) Prepare the response:
        #    - message_size (4 bytes) = 4
        #    - correlation_id (4 bytes) = 7
        #
        #    We’ll pack these as two big-endian 32-bit integers (">ii").
        response = struct.pack(">ii", 4, 7)

        # 3) Send the response to the client
        conn.sendall(response)
        print("Sent 8-byte response (message_size=4, correlation_id=7)")

        # 4) Close the connection
        conn.close()

if __name__ == "__main__":
    main()
