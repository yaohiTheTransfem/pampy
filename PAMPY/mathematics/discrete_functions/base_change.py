def base_change(a, b):
    try:
        if int(a) != a or int(b) != b:
            raise ValueError
    except ValueError:
        return "NAN"
    return_value = ""
    quotient = a
    while quotient != 0:
        remaider = quotient % b
        return_value += str(remaider)
        quotient //= b
    return return_value[::-1]



def complex_base_change(a, b):
    pass

def fractional_base_change(a, b):
    pass
if __name__ == "__main__":
    print(base_change(2 ** 16, 2))  # [1, 0, 1, 0]
    print(base_change(983040, 16))  # [15, 15]
    print(base_change(100, 8))  # [1, 4, 4]
    print(base_change(10.5, 2))  # "NAN"
