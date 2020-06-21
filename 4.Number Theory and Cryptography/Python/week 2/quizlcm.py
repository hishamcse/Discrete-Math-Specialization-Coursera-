def lcm(a, b):
    assert a > 0 and b > 0

    def gcdeuclidanother(a, b):
        return gcdeuclidanother(b, a % b) if b > 0 else a

    return (a * b) // gcdeuclidanother(a, b)


print(lcm(2108312, 193271))
