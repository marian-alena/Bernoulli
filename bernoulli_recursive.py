from fractions import Fraction
import math


def bernoulli_recursive(n: int) -> list[Fraction]:
    """Generates B_0 through B_n (with B_1 = -1/2) using memoized recursion."""
    b = [Fraction(0)] * (n + 1)
    b[0] = Fraction(1)

    for m in range(1, n + 1):
        # Odd Bernoulli numbers > 1 are always 0
#        if m > 1 and m % 2 == 1:
#            continue
        total = sum(math.comb(m + 1, k) * b[k] for k in range(m))
        b[m] = -Fraction(total, m + 1)

    return b

n = 500
b = bernoulli_recursive(n)
for index, value in enumerate(b):
    print(f"B_{index} = {value}")
