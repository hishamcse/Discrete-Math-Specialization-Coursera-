# not efficient algorithm
def lcd(a, b):
    assert a > 0 and b > 0

    for i in range(1, a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


print(lcd(24, 16))


# most efficient algorithm
def gcdeuclidanother(a, b):
    assert a >= b >= 0 and a >= 0
    return gcdeuclidanother(b, a % b) if b > 0 else a


def lcm(a, b):
    if a >= b:
        return (a * b) // gcdeuclidanother(a, b)
    else:
        return (a * b) // gcdeuclidanother(b, a)


print(lcm(243485, 16712674825))
