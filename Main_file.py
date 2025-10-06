##This script will contain multiple functions for computing physics and math stuff
##try categorize the functions by fields of stufy, and their respective field
##for constants used in other functions set their x value to the value that nothing changes due to python's decimal number limitations
##pampy is an shorthand for "physics and mathematics formulae python"

##basic arithmetic 
##all of these are made for fun, delete if you want!
def add(x, y):
    return x+y
def sub(x, y):
    return -y+x
def mul(x, y):
    return x*y
def div(x, y):
    return 1/y*x

##intermediate functions
def factorial(x): ##only can take in positive integer inputs, use gamma function for negative or fractional values
    total = 1 
    if x == 0:
        return total
    else: 
        for ite in range(1, x):
            total *= ite 
        return total*x
def N_factorial(x, y):

##store section for roots, factorials etc

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
    return 0.083333333 * total ** -1

def gold_ratio():
    return ((sqrt(5)+1)*0.5)


##beginner functions









##number theory
def triangular_num(x):
    return x*(x+1)*0.5


##statistics
def arithmetic_mean(x):
    n = len(x)
    sum = 0
    for ite in range(n):
        sum += x[ite]
    return sum*1/n
def binomial_coefficient(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def binomial_theorem(x, y, n):
    k = 0
    total = 0
    for ite in range(n):
        total += (x ** ite)*(y ** (n-k))
    return total

##euclidean geometry
def area_square(a):
    return a ** 2

def area_rectangle(l, h):
    return l * h

def area_triangle(a):
    return (a ** 2)/2

def area_circle(r):
    return pi(4)*(r**2)

def perimetre_square(l): ##l is is the length of one of the four sides in the square
    return l*4













##Trigonometry functions
def deg_to_rad(x):
    return pi(4)*0.00555555555*x

def rad_to_deg(x):
    return x*180*(1/(pi(5)))

def sin(x):

def tan(x):

def cos(x):
    









##non beginner based composed functions
##lambert W function
def W(z):
    return z*(e(64)**z)
