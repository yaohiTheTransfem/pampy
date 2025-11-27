from math.math_formulae import factorial

##classical mechanics
def force(m, a):
    return m*a

def final_velocity(u, a, t):
    return u + (a * t)

def momentum(m, v):
    return m * v

def impulse(f, d, t):
    return f * d * t

def kinetic_energy(m, v):
    return 0.5 * (m * (v ** 2))

def potiental_energy(m, g, h):
    return m * g * h

def work_energy(f, d):
    return f * d

def centripetal_force(m, v, r):
    return ((m * (v ** 2))/r)

def torque(i, a):
    return a * i