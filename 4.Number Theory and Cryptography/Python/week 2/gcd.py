def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0
    if a == 0 or b == 0:
        return max(a, b)
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        return 1


print(gcd(289, 4))


# efficient algorithm but slow
def gcdeuclid(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a - b
        else:
            b = b - a

    return max(a, b)


print(gcdeuclid(289, 4))


# more efficient algorithm and fast
def gcdeuclideff(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    return max(a, b)


print(gcdeuclideff(23975973421233124, 4))


# another efficient algorithm
def gcdeuclidanother(a, b):
    assert a >= b >= 0 and a >= 0
    return gcdeuclidanother(b, a % b) if b > 0 else a


print(gcdeuclideff(23975973421233124, 4))
