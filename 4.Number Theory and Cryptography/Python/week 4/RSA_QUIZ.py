def ConvertToInt(message_str):
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res


def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def extended_gcd(a, b):
    assert a >= b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        d, p, q = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return d, x, y


def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def PowMod(a, n, modulo):
    assert modulo > 1 and a > 0 and gcd(a, modulo) == 1

    if a >= modulo:
        d, s, t = extended_gcd(a, modulo)
    else:
        d, t, s = extended_gcd(modulo, a)
    if s < 0:
        s = modulo + s
    return (n * s) % modulo


# identical to PowMod
def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1

    if a >= n:
        d, s, t = extended_gcd(a, n)
    else:
        d, t, s = extended_gcd(n, a)
    if s < 0:
        s = n + s
    return (b * s) % n


def InvertModulo(a, b):
    return PowMod(a, 1, b)


# quiz 1
def Encrypt(message, modulo, exponent):
    return PowMod(ConvertToInt(message), exponent, modulo)


# quiz 2
def Decrypt(ciphertext, p, q, exponent):
    d = InvertModulo(exponent, (p - 1) * (q - 1))
    return ConvertToStr(PowMod(ciphertext, d, p * q))


a = 3
b = 7
c = InvertModulo(a, b)
print(c)

p = 1000000007
q = 1000000009
exponent = 23917
modulo = p * q
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
message = Decrypt(ciphertext, p, q, exponent)
print(message)


# quiz 3
def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    # Fix this implementation
    for i in range(len(potential_messages)):
        if ciphertext == Encrypt(potential_messages[i], modulo, exponent):
            return potential_messages[i]
    return "don't know"


modulo = 101
exponent = 12
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSimple(ciphertext, modulo, exponent, ["attack", "don't attack", "wait"]))


# quiz 4
def DecipherSmallPrime(ciphertext, modulo, exponent):
    for m in range(3, 1000000):
        if modulo % m == 0:
            small_prime = m
            big_prime = modulo // m
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return "don't know"


modulo = 101 * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
exponent = 239
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSmallPrime(ciphertext, modulo, exponent))

# quiz 5
import math


def IntSqrt(modulo):
    return int(math.sqrt(modulo))


def DecipherSmallDiff(ciphertext, modulo, exponent):
    for i in range(IntSqrt(modulo) - 5000, IntSqrt(modulo) + 1):
        if modulo % i == 0:
            small_prime = i
            big_prime = modulo // i
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return None


p = 1000000007
q = 1000000009
n = p * q
e = 239
ciphertext = Encrypt("attack", n, e)
message = DecipherSmallDiff(ciphertext, n, e)
print(ciphertext)
print(message)


# quiz 6
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                          second_exponent):
    # Fix this implementation to correctly decipher both messages in case
    # first_modulo and second_modulo share a prime factor, and return
    # a pair (first_message, second_message). The implementation below won't work
    # if the common_prime is bigger than 1000000.
    common_prime = GCD(first_modulo, second_modulo)
    q1 = first_modulo // common_prime
    q2 = second_modulo // common_prime
    return (Decrypt(first_ciphertext, common_prime, q1, first_exponent),
            Decrypt(second_ciphertext, common_prime, q2, second_exponent))


# Example usage with common prime p and different second primes q1 and q2
p = 101
q1 = 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
q2 = 1000000007
first_modulo = p * q1
second_modulo = p * q2
first_exponent = 239
second_exponent = 17
first_ciphertext = Encrypt("attack", first_modulo, first_exponent)
second_ciphertext = Encrypt("wait", second_modulo, second_exponent)
print(DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                            second_exponent))


# quiz 7
def ChineseRemainderTheorem(n1, r1, n2, r2):
    def ExtendedEuclid(n1, n2):
        x = divide(n1, 1, n2) * n1 * r2
        y = divide(n2, 1, n1) * n2 * r1

        return x, y

    (x, y) = ExtendedEuclid(n1, n2)

    return (x + y) % (n1 * n2)


def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
    # Fix this implementation
    r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
    return ConvertToStr(IntSqrt(r))


p1 = 790383132652258876190399065097
q1 = 662503581792812531719955475509
p2 = 656917682542437675078478868539
q2 = 1263581691331332127259083713503
n1 = p1 * q1
n2 = p2 * q2
ciphertext1 = Encrypt("attack", n1, 2)
ciphertext2 = Encrypt("attack", n2, 2)
message = DecipherHastad(ciphertext1, n1, ciphertext2, n2)
print(message)
