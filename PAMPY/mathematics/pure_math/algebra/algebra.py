from mathematics.countinous_functions.roots.roots import sqrt
def quadratic(a, b, c):
    total = (sqrt((b * b)- (4*a*c))*(1/(2*int(a))))
    neg = -(b + total)
    pos = -(b - total)
    return neg, pos

print(quadratic(3, 4, 5))

