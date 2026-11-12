from fractions import Fraction


def generate_bernoulli(n: int) -> list[Fraction]:
    """
    Akiyama–Tanigawa Algorithm
    Generates Bernoulli numbers B_0 through B_n as exact fractions.
    """
    a = [Fraction(1, m + 1) for m in range(n + 1)]
    bernoulli = []

    for m in range(n + 1):
        bernoulli.append(a[0])
        for j in range(n - m):
            a[j] = (j + 1) * (a[j] - a[j + 1])

    return bernoulli


# Example: Print B_0 through B_n
n = 500
b = generate_bernoulli(n)
for index, value in enumerate(b):
    print(f"B_{index} = {value}")
