from mathematics.constants import pi
##euclidean geometry
def area_square(a):
    return a ** 2

def area_rectangle(l, h):
    return l * h

def area_triangle(l, h):
    return (l * h)/2

def area_circle(r):
    return pi()*(r * r)

def perimetre_square(l): ##l is is the length of one of the four sides in the square
    return l*4