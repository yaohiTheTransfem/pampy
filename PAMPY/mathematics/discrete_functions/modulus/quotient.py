
def reciprocal_quotient(b): ##finds the integer quotient of 1/b
    negative = False
    length = len(str(b))
    multiplier = 0
    
    try:
        
        if b == 0:
            raise ZeroDivisionError ###handles division by zero and returns NaN
        elif b < 0:
            negative = True
            b = abs(b)
        
        
        
        ##fetches the scaled version of 1/b
        scaled_ten = "10"
        for i in range(int(length)-1):
            scaled_ten += "0"
        scaled_ten = int(scaled_ten)
            
        ##finds the largest multiple of b that is less than scaled_ten
        while b * multiplier <= scaled_ten:
            multiplier += 1
        guess = multiplier - 1
        regex = "0."
        regex += str(guess)
        guess = float(regex)
        
        
        if negative:
            return -guess
        else:
            return guess
    
    except ZeroDivisionError:
        return "NaN"




if __name__ == "__main__":
    print(reciprocal_quotient(3456789))
