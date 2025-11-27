from quotient import quotient
def remaider(a, b):
    remaider = a - b * quotient.quotient(a, b)
    return remaider

def python_negative_remainder(a, b):
    return a % b