"""Python non-prime generators"""


import math


def is_prime_number(n):
    if (n <= 1):
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if (n % 2 == 0):
        return False

    m = 3
    while (m <= math.sqrt(n)):
        if (n % m == 0):
            return False
        m += 2
    return True


def manipulate_generator(generator, n):
    # Enter your code here
    if is_prime_number(n + 1):
        next(generator)
        manipulate_generator(generator, n + 1)


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)
