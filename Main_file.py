##This script will contain multiple functions for computing physics and math stuff
##try categorize the functions by fields of stufy, and their respective field
##for constants used in other functions set their x value to the value that nothing changes due to python's decimal number limitations
##pampy is an shorthand for "physics and mathematics formulae python"

##discrete
##statistics
def arithmetic_mean(x):
    n = len(x)
    sum = 0
    for ite in range(n):
        sum += x[ite]
    return sum/n
        
##combinatorics
def factorial(x): ##only can take in positive integer inputs, use gamma function for negative or fractional values
    total = 1 
    if x == 0:
        return total
    else: 
        for ite in range(1, x):
            total *= ite 
        return total*x

def binomial_coefficient(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def binomial_theorem(x, y, n):
    k = 0
    total = 0
    for ite in range(n):
        total += (x ** ite)*(y ** (n-k))
    return total




##countinous
##constants
def e(x):
    total = 0
    k = 1
    for ite in range(x):
        reciprocal = 1/(k * (2 ** k)) 
        k += 1
        total += reciprocal
    return 2**(1/total)

def pi(x):
    total = 0
    for ite in range(x):
       total += (((-1)**ite)*((factorial(6*ite))/((factorial(3*ite))*(factorial(ite))**3))*((13591409 + 54514013 * ite)/(640320 ** (3 * ite + 1.5))))
    return 1/12 * total ** -1


##non beginner based composed functions
##lambert W function
def W(z):
    return z*(e(64)**z)


test = binomial_coefficient(5, 2)
print(f"The value for the binomial coefficient function is {test}")
