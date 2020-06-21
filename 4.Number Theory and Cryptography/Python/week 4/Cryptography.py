# m is the message,k is the random secret key which is known to only message sender and receiver
# at encryption, c is passed which is the xor of m and k.
# at decryption, c is received which decrypts using another xor operation of c and k.
# so, c XOR k = m XOR k XOR k = m.


def message_encrypt(m, k):
    return m ^ k


def message_decrypt(c, k):
    return c ^ k


def highest_number_generator(m):
    n = bin(m)
    h = 0
    for i in range(0, len(n) - 2):
        h = h + pow(2, i)
    return h


import random

# print(message_encrypt(19237, 9864))
# print(message_decrypt(message_encrypt(19237, 9864),9864))

m = 19237
k = random.randint(1, highest_number_generator(m))  # as we need a random number of which has at most the number of bits as m have
print("cipher code ", k)
print("encrypted code ", message_encrypt(m, k))
print(message_decrypt(message_encrypt(m, k), k))
