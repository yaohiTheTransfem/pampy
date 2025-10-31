import operators
def comp_e(x):
    total = 0
    k = 1
    for ite in range(x):
        reciprocal = 1/(k * (2 ** k))
        k += 1
        total += reciprocal
    return 2**(1/total)


def comp_pi(x):
    total = 0
    for ite in range(x):
       total += (((-1)**ite)*((operators.factorial(6*ite))/((operators.factorial(3*ite))*(operators.factorial(ite))**3))*((13591409 + 54514013 * ite)/(640320 ** (3 * ite + 1.5))))
    return 0.083333333 * total ** -1


def pi():
    return 3.141592641023371


def gold_ratio():
    return 1.618033988749895

def comp_gold_ratio():
    return ((operators.sqrt(5) + 1) * 0.5)


def e():
    return 2.718281828459046

print(gold_ratio())

