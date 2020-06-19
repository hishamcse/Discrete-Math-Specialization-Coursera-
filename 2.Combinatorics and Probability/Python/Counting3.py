# salad
from itertools import combinations_with_replacement
count = 0
for i in combinations_with_replacement("TLAD", 7):
    print("".join(i))
    count += 1
print(count)

# Numbers with fixed sum of digits
from itertools import product

count = 0
for i in product(range(10), repeat=4):
    if i[0] + i[1] + i[2] + i[3] == 10:
        print(i)
        count += 1
print(count)

# Numbers with non-increasing digits
count = 0
for i in product(range(10), repeat=4):
    if i[0] >= i[1] >= i[2] >= i[3]:
        count += 1
print(count)
