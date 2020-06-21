# def FastModularExponentiation(b, k, m):
#     c = b
#     for i in range(1, k + 1):
#         c = c % m
#         c = c * c
#     return c % m


# print(FastModularExponentiation(7, 7, 11))


def Modular_Exponentiation_Power(b, k, m):
    c = b
    for i in range(1, k + 1):
        c = c % m
        c = c * c
    return c % m


def FastModularExponentiation(b, e, m):
    a = 1
    print(bin(e))
    n = bin(e)
    for i in range(len(n) - 1, 1, -1):
        if int(n[i]) != 0:
            a = a * Modular_Exponentiation_Power(b, len(n)-1-i, m)
    return a % m


print(FastModularExponentiation(7, 13, 11))
print(FastModularExponentiation(2, 238, 239))
print(FastModularExponentiation(2, 953, 239))
print(FastModularExponentiation(34, 60, 77))
