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


def ChineseRemainderTheorem(n1, r1, n2, r2):
    def ExtendedEuclid(n1, n2):
        x = divide(n1, 1, n2) * n1 * r2
        y = divide(n2, 1, n1) * n2 * r1

        return x, y

    (x, y) = ExtendedEuclid(n1, n2)

    return (x + y) % (n1 * n2)


print(ChineseRemainderTheorem(686579304, 295310485, 26855093, 8217207))
