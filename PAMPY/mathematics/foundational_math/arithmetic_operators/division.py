from mathematics.discrete_functions.modulus.quotient import reciprocal_quotient
def newton_division(a, b, iterations=10):
    x = reciprocal_quotient(b)  ##returns 1 decimal place of 1/b
    for iterations in range(iterations):
        x = x - (b * x - 1) * x ##newton's method formula
    return a*x

print(newton_division(10, 3))