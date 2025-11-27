import numbers








def binomial_coefficient(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))


def binomial_theorem(x, y, n):
    k = 0
    total = 0
    for ite in range(n):
        total += (x ** ite)*(y ** (n-k))
    return total

def root(n, m):
    recip = 1/m
    guess = recip * n
    for ite in range(100):
        guess = (((guess + (n/guess)) * recip) ** (m-1))
    return guess




"""
def simplify_frac(a, b):
    a_factors = number_theory.factor(a)
    b_factors = number_theory.factor(b)
    for ite in range(len(a)):
        try:
        except IndexError:
            return f"{a/b} is the simplified fraction"
"""