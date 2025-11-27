def triangular_num(x):
    return x*(x+1)*0.5



def factor(n):
    factors = []
    for ite in range(1, n):
        if n % ite == 0:
            factors.append(ite)
        else:
            pass
    return factors
