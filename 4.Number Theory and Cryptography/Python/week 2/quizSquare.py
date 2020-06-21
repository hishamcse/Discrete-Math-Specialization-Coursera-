def gcdeuclidanother(a, b):
    assert a >= b >= 0 and a >= 0
    return gcdeuclidanother(b, a % b) if b > 0 else a


def squares(n, m):
    if (n >= m):
        return (n * m) // (gcdeuclidanother(n, m) * gcdeuclidanother(n, m))
    else:
        return (n * m) // (gcdeuclidanother(m, n) * gcdeuclidanother(m, n))


print(squares(6, 10))
