import random
import math
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

upper_bound = 10**30
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    prime = random.randint(100, upper_bound)
    while not is_prime(prime):
        prime = random.randint(100, upper_bound)
    return prime

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair():
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def encrypt(message, public_key):
    n, e = public_key
    cipher_text = pow(message, e, n)
    return cipher_text

def decrypt(cipher_text, private_key):
    n, d = private_key
    plain_text = pow(cipher_text, d, n)
    return plain_text

def main2():
    keyPair = RSA.generate(3072)

    pubKey = keyPair.publickey()
    print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
    pubKeyPEM = pubKey.exportKey()
    print(pubKeyPEM.decode('ascii'))

    print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")



def main():
    public_key, private_key = generate_keypair()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = int(input(f"Enter The message : "))

    cipher_text = encrypt(message, public_key)
    print("Encrypted:", cipher_text)

    decrypted_message = decrypt(cipher_text, private_key)
    print("Decrypted:", decrypted_message)

if __name__ == "__main__":
    main2()