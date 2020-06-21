def gcd(a, b):
    assert a >= b >= 0 and a >= 0
    return gcd(b, a % b) if b > 0 else a


# N*log2(N)
def Euler_Totient(n):
    c = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            c += 1
    return c


# print(Euler_Totient(276234))


# Python3 program to calculate
# Euler's Totient Function(effective and fast)
# (sqrt(N)*logM(N))+1
def Euler_Totient_Fast(n):
    # Initialize result as n
    result = n

    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    m = 2
    while m * m <= n:

        # Check if p is a
        # prime factor.
        if n % m == 0:

            # If yes, then
            # update n and result
            while n % m == 0:
                n = int(n / m)
            result -= int(result / m)
        m += 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most
    # one such prime factor)
    if n > 1:
        result -= int(result / n)
    return result


print(Euler_Totient_Fast(276234))
print(Euler_Totient(77))
