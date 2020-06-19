# # factorial
#
# def factorial(n):
#     assert n > 0
#     if (n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))


# # coin problem (3,5)  (minimum 3 conditions as the lower number is 3)
# def coin(amount):
#     assert amount >= 8
#     if amount == 8:
#         return [3, 5]
#     if amount == 9:
#         return [3, 3, 3]
#     if amount == 10:
#         return [5, 5]
#
#     coins = coin(amount - 3)
#     coins.append(3)
#     return coins
#
# print(coin(102))

# coin problem (7,5)(minimum 5 conditions as lower number 5 and maximum 7 as higher number 7)
# def change(amount):
#     assert amount >= 10
#     if amount == 12:
#         return [5, 7]
#     if amount == 10:
#         return [5, 5]
#     if amount == 14:
#         return [7, 7]
#     if amount == 15:
#         return [5, 5, 5]
#     if amount == 17:
#         return [5, 5, 7]
#     if amount == 19:
#         return [5, 7, 7]
#     if amount == 21:
#         return [7, 7, 7]
#
#     coins = change(amount - 5)
#     coins.append(5)
#     return coins
#
# print(change(49))  # largest impossible number is 23.above that ,every integer is a solution

# coin problem second quiz solution code(minimum 5 conditions)
# def change(amount):
#     assert amount >= 24
#     if amount == 24:
#         return [5, 5, 7, 7]
#     if amount == 25:
#         return [5, 5, 5, 5, 5]
#     if amount == 26:
#         return [7, 7, 7, 5]
#     if amount == 27:
#         return [5, 5, 5, 5, 7]
#     if amount == 28:
#         return [7, 7, 7, 7]
#
#     coin = change(amount - 5)
#     coin.append(5)
#     return coin

# print(change(49))

# tower of hanoy(minimum moves)  the theme is one disc has to move minimum same as the total discs quantity.
# and the the biggest disc will move 1 time less
discs = input()
totalmoves = pow(2, int(discs)) - 1
print(totalmoves)


# tower of hanoy(effective solution)
def hanoi(n, src, temp, dest):
    if n == 1:
        return 1

    return hanoi(n - 1, src, dest, temp) + \
           hanoi(1, src, temp, dest) + \
           hanoi(n - 1, temp, src, dest)


print(hanoi(6, src=1, temp=2, dest=3))
