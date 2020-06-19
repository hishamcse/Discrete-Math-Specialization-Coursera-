# n = 10
# count = 0
#
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             if i < j and j < k:
#                 count += 1
#
# print(count)

# Pascal's Triangle
# c = dict()
# for n in range(9):
#     c[n, 0] = 1
#     c[n, n] = 1
#
#     for k in range(1, n):
#         c[n, k] = c[n - 1, k - 1] + c[n - 1, k]
# print(c[8, 4])
# print(c[6, 4])

# practice counting (see slide-present at least one 7 in 4 digits)
from itertools import product

count = 0
for i in product(range(10), repeat=4):   # all the numbers using 4 digits
    if 7 in i:                           # if 7 is present in the numbers
        count = count + 1
print(count)

# practice counting (numbers having increasing digits)
count = 0
for i in product(range(10), repeat=4):
    if i[0] < i[1] < i[2] < i[3]:
        count += 1
print(count)
