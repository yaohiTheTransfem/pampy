def arithmetic_mean(x):
    n = len(x)
    sum = 0
    for ite in range(n):
        sum += x[ite]
    return sum*1/n