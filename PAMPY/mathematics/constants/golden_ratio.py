from mathematics.countinous_functions.roots.roots import sqrt
from mathematics.discrete_functions.factorial.factorial import factorial
import sys
print("Loaded:", __name__, "→", sys.modules.get(__name__))

def comp_e(x):
    total = 0
    k = 1
    for ite in range(x):
        reciprocal = 1/(k * (2 ** k))
        k += 1
        total += reciprocal
    return 2**(1/total)




def comp_gold_ratio():
    return ((sqrt(5) - 1) * 0.5)

def comp_tau(x):
    total = 0
    for ite in range(x):
       total += (((-1)**ite)*((factorial(6*ite))/((factorial(3*ite))*(factorial(ite))**3))*((13591409 + 54514013 * ite)/(640320 ** (3 * ite + 1.5))))
    return 2 * 0.083333333 * total ** -1











def pi():
    return 3.141592641023371

def gold_ratio():
    return 1.618033988749895

def gamma_const():
    return 0.5772156649015328

def e():
    return 2.718281828459046

def tau():
    return 6.283185282046742

