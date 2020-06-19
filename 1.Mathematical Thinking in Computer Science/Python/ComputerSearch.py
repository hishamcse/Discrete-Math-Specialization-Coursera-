# N queens algorithm(first way)-Brute Force
import itertools as it


def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):  # means tuples consisting of 2 members between 0-7
        # print(i1,i2)
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True


count = 0
for perm in it.permutations(range(8)):
    # print(perm)
    if is_solution(perm):
        print(perm)  # printing all possible solutions,that's why,we didnt exit
        count = count + 1
        # exit()
print("Total solution is:", count)
