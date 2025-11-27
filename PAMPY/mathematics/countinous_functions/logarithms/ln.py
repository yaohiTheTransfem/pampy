

def ln(x, iterations=1000):
    if x < 1:
        return -ln(1 / x, iterations)
