import socket

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Client: Requesting key exchange...")
    P, G = map(int, client_socket.recv(1024).decode().split())
    print(f"Client: Received Prime Number P = {P} and Generator G = {G}")


    X = int(input(f"Enter The key : "))

    while 1:
        if X >= P:
            print(f"Private Key Of User Should Be Less Than {P}!")
            continue
        break

    R1 = (G ** X) % P
    client_socket.send(f"{R1}".encode())
    print(f"Client: Sending R1 = {R1} to Server")

    R2 = int(client_socket.recv(1024).decode())
    print("Client: Received R2 =", R2)

    secret_key = (R2 ** X) % P
    print("Client: Symmetric Key =", secret_key)

    client_socket.close()

if __name__ == "__main__":
    main()