import socket
import subprocess
addr = ("add.ip.address.here", 5433)

with socket.create_server(addr, family=socket.AF_INET) as s:
    print("Server is running and waiting for a connection...")
    while True:
        conn, client_addr = s.accept()
        print(f"Connected to {client_addr}")

        with conn:
            data = conn.recv(1024)
            if data:
                print("Received:", data.decode())  # Decode bytes to text
                
                while True:
                    test = input("Run commands: ")
                    conn.send(test.encode())  # Send response back to client