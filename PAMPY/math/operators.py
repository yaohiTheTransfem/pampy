def sqrt(n):
    complex = 0
    if n < 0:
        complex += 1
        n = abs(n)
    else:
        pass
    guess = 0.5 * n
    for ite in range(8):
        guess = ((guess + (n/guess)) * 0.5)
    if complex == 1:
        return f"{guess}i"
    else:
        return guess

def factorial(x): ##only can take in positive integer inputs, use gamma function for negative or fractional values
    total = 1 
    if x == 0:
        return total
    else: 
        for ite in range(1, x):
            total *= ite 
        return total*x


def N_factorial(x, y):
    pass

def binomial_coefficient(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))


def binomial_theorem(x, y, n):
    k = 0
    total = 0
    for ite in range(n):
        total += (x ** ite)*(y ** (n-k))
    return total