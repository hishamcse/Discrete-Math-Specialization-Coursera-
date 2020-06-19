# 16 diagonal(very difficult)-backtracking
def extend(Diag, n):
    if len(Diag) == n * n:
        print(Diag)
    choice = [0, 1, 2]
    for Diag_k in choice:
        Diag.append(Diag_k)
        if check_if_Diag_can_be_extended(Diag, n):
            extend(Diag, n)
        Diag.pop()


def check_if_Diag_can_be_extended(Diag, n):
    k = len(Diag)
    # Check the first row
    if k <= n:
        if Diag[k - 1] * Diag[k - 2] == 2:
            return False
    # check the first column but not first row
    if k > n and k % n == 1:
        if Diag[k - 1] * Diag[k - n - 1] == 2 or Diag[k - 1] * Diag[k - n] == 1:
            return False
    # check the last column but not first row
    if k > n and k % n == 0:
        if Diag[k - 1] * Diag[k - 2] == 2 or Diag[k - 1] * Diag[k - n - 1] == 2 or Diag[k - 1] * Diag[k - n - 2] == 4:
            return False
    # check others
    if k > n and k % n != 0 and k % n != 1:
        if Diag[k - 1] * Diag[k - 2] == 2 or Diag[k - 1] * Diag[k - n - 1] == 2 or Diag[k - 1] * Diag[k - n] == 1 or \
                Diag[k - 1] * Diag[k - n - 2] == 4:
            return False
    # satisfy empty cells <=n^2-16
    if Diag.count(0) > n * n - 16:
        return False
    return True


# 0 represents empty, 1 represents '/',2 represents '\'
extend(Diag=[], n=5)
