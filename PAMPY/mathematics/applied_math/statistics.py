def arithmetic_mean(x):
    n = len(x)
    sum = 0
    for ite in range(n):
        sum += x[ite]
    return sum*1/n

def geometric_mean(n):
    total = 1
    length = len(n)
    for ite in range(length):
        total *= n[ite]

def harmonic_mean(n):
    m = len(n)
    total = 0
    for ite in range(m):
        total += 1/n[ite]
    return m * (1/total)

