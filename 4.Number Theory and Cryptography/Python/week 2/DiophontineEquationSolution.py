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


def diophantine(a, b, c):
    assert c % gcd(a, b) == 0
    l = c // gcd(a, b)
    if a >= b:
        d, x, y = extended_gcd(a, b)
    else:
        d, y, x = extended_gcd(b, a)

    return (l * x, l * y)


print(diophantine(10, 6, 14))
print(diophantine(391, 299, -69))


# for all solutions (t is any valid solved value ranged from the inequality solution and n is the first solution,
# x is the minimum value that t can have.if t is less than x,then there is no solution) coefficients are the value of
# a and b in the equation
def anySolutiontodiophantine(x, t, coeffecient, n):
    assert t >= x
    d = gcd(coeffecient[0], coeffecient[1])
    p = coeffecient[0] // d
    q = coeffecient[1] // d

    return (n[0] + t * q), (n[1] - t * p)


n = diophantine(10, 6, 14)
coeffecient = (10, 6)
print(anySolutiontodiophantine((7 / 3), 3, coeffecient, n))
