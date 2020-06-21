def Modular_Exponentiation_Power(b, k, m):
    c = b
    for i in range(1, k + 1):
        c = c % m
        c = c * c
    return c % m


def FastModularExponentiation(b, e, m):
    a = 1
    # print(bin(e))
    n = bin(e)
    for i in range(len(n) - 1, 1, -1):
        if int(n[i]) != 0:
            a = a * Modular_Exponentiation_Power(b, len(n) - 1 - i, m)
    return a % m


def extended_gcd(a, b):
    assert a >= b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        d, p, q = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return d, x, y


def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1

    if a >= n:
        d, s, t = extended_gcd(a, n)
    else:
        d, t, s = extended_gcd(n, a)
    if s < 0:
        s = n + s
    return (b * s) % n


def encryption(m, n, e):
    z = int(m.encode('utf-8').hex(), 16)
    print(m.encode('utf-8').hex())
    # print(int(m.encode('utf-8').hex(), 16))
    return FastModularExponentiation(z, e, n)


def decryption(p, q, e, c):
    d = divide(e, 1, (p - 1) * (q - 1))
    return FastModularExponentiation(c, d, n)


import random

while True:
    random.seed(None,2)
    p = random.randint(1000000, 1000000000)
    q = random.randint(1000000, 1000000000)
    if abs(p - q) >= 10000000:
        break

n = p * q

while True:
    e = random.randint(1000000, (p - 1) * (q - 1))
    if gcd(e, (p - 1) * (q - 1)) == 1:
        break

# def generate_RSA(bits=2048):
#     '''
#     Generate an RSA keypair with an exponent of 65537 in PEM format
#     param: bits The key length in bits
#     Return private key and public key
#     '''
#     from PyOpenSSLContext
#     from crypto.PublicKey import RSA
#     new_key = RSA.generate(bits, e=65537)
#     public_key = new_key.publickey().exportKey("PEM")
#     private_key = new_key.exportKey("PEM")
#     return private_key, public_key

encrypt = encryption("Hello World", n, e)
print(encrypt)
decrypt = decryption(p, q, e, encrypt)
print(decrypt)
print(hex(decrypt))
