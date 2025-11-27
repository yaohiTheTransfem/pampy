import sys
print("Loaded:", __name__, "→", sys.modules.get(__name__))


def euler_infinite_product_gamma(z, iterations):
    total = 1
    for ite in range(1, iterations):
        reciprocal = 1/ite
        total *= (1/(1+(reciprocal * z)) * ((1 + reciprocal) ** z))
    total *= 1/z
    return total
