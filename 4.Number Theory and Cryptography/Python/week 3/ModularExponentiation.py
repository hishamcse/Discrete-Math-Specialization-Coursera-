# straight forward(not effecient)
def Modular_Exponentiation(b, e, m):
    c = 1
    for i in range(1, e + 1):
        c = (c * b) % m
    return c


print(Modular_Exponentiation(7, 4, 11))

# fast when e is a power of 2 (just need a constant k time.log2e=k)
import math


def Modular_Exponentiation_Power(b, e, m):
    c = b
    step = int(math.log(e) / math.log(2))
    for i in range(1, step + 1):
        c = c % m
        c = c * c
    return c % m


print(Modular_Exponentiation_Power(7, 128, 11))
