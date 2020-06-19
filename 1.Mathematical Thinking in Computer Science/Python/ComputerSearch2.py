# N queens algorithm(effecient way)-backtracking
def can_extend_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if (i - j) == abs(perm[i] - perm[j]):
            return False
    return True


def extend(perm, n):
    if (len(perm) == n):
        print(perm)
        quit()

    for k in range(n):
        if k not in perm:
            perm.append(k)
            if can_extend_to_solution(perm):
                extend(perm, n)

            perm.pop()


extend(perm=[], n=25)
