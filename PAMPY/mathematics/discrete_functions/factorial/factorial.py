def factorial(x): ##only can take in positive integer inputs, use gamma function for negative or fractional values
    total = 1
    if x < 0 or int(x)-x !=0:
        pass ##return gamma(x)
    elif x == 0:
        return total
    else: 
        for ite in range(1, (x+1)):
            total *= ite 
        return total

def n_factorial(x, y):
    def even_factorial(x, y, z):
        non_local_total = 1
        for ite in range((x//y)+z):
            non_local_total *= x-(ite*y) 
        return non_local_total
    
    total = 1
    if x < 0 or int(x)-x !=0:
        pass ##return gamma(x)
    elif x % 2 == 0: 
        
        if y % 2 != 0:
            return even_factorial(x, y, 1)
        else:
            return even_factorial(x, y, 0)
    
    else:
        for ite in range(0, x, y):
            total *= x - ((ite + 1) * y)  
        return total

print(f"The factorial is {n_factorial(9 , 3)}")