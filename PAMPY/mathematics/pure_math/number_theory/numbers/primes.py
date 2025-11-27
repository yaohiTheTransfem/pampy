import sys
sys.path.append('C:\Users\yaohi\OneDrive\Documents\personal_stuff\Projects for work\math\computer_stuff\programming\Python_program\Math_stuff\PAMPY\mathematics\discrete_functions\floor.py')


def is_prime(n):
    if n<0:
        return "Please use the gaussian primes function instead"
    elif n in [0, 1]:
        return f"{n} is a unit"
    for ite in range(2, floor(sqrt(n)+1)):
        if n % (ite) == 0:
            return f"{n} is not a prime number"
        else:
            pass
    return f"{n} is a prime number"

def prime(n):
    prime_counter = 1
    ite = 1
    while prime_counter != n:
        for j in range(2, floor(sqrt(ite)+1)):
            if ite % (j) == 0:
                ite += 1
                break
            else:
                pass
        prime_counter += 1
        ite += 1

