import socket
import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_checker(p):
    # Checks If the number entered is a Prime Number or not
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
            return 1

def primitive_check(g, p, L):
    # Checks If The Entered Number Is A Primitive Root Or Not
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
        return 1
def mod_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server: Waiting for a connection...")
    client_socket, addr = server_socket.accept()
    print("Server: Connection established with", addr)

    while 1:
        P = int(input("Enter P : "))
        if prime_checker(P) == -1:
            print("Number Is Not Prime, Please Enter Again!")
            continue
        break

    l = []

    # while 1:
    G = int(input(f"Enter The Primitive Root Of {P} : "))
        # if primitive_check(G, P, l) == -1:
        #     print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
        #     continue
        # break



    x1 = int(input(f"Enter The key : "))

    while 1:
        if x1 >= P:
            print(f"Private Key Of User Should Be Less Than {P}!")
            continue
        break

    y1 = pow(G, x1) % P

    client_socket.send(f"{P} {G}".encode())

    R1 = int(client_socket.recv(1024).decode())
    print("Server: Received R1 =", R1)

    R2 = mod_pow(G, y1, P)
    client_socket.send(f"{R2}".encode())

    secret_key = mod_pow(R1, y1, P)
    print("Server: Symmetric Key =", secret_key)

    print("Server: Key exchange sucessfull")

    server_socket.close()
    client_socket.close()

if __name__ == "__main__":
    main()