def sqrt(n):
    is_complex = 0
    if n < 0:
        is_complex += 1
        n = abs(n)
    else:
        pass
    guess = 0.5 * n
    for ite in range(8):
        guess = ((guess + (n/guess)) * 0.5)
    if is_complex == 1:
        return f"{guess}i"
    else:
        return guess

