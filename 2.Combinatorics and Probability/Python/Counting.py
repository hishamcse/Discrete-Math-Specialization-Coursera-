c = 0
for i in range(1, 1001):
    if i % 2 == 0 or i % 3 == 0:
        c = c + 1
print(c)

# permutation
from itertools import permutations

for p in permutations("abcdef", 3):
    print("".join(p))

# number of games played
from itertools import combinations

k = 0
for c in combinations("abcdefgh", 2):
    print("".join(c))
    k = k + 1
print(k)


# number of games played (recursion)
def t(n):
    if n <= 1:
        return 0
    return (n - 1) + t(n - 1)


print(t(8))
