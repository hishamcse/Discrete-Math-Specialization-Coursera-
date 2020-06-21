str = "Hello World".encode('utf-8')
print(str.hex())
print(str.decode())
print(bytes.fromhex(str.hex()))

import random
import string


def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def message_encrypt(m, k):
    return int(m.encode('utf-8').hex(), 16) ^ int(k.encode('utf-8').hex(), 16)


def message_decrypt(c, k):
    return int(c, 16) ^ int(k.encode('utf-8').hex(), 16)


r = randomString(len("Hello world"))
hex_str = hex(message_encrypt("Hello World", r))
print(hex_str)
print(hex(message_decrypt(hex_str, r)))
