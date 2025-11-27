def congruence(a, b, n):
    try:
        if a % n == b % n:
            return True
        else:
            return False
    except ZeroDivisionError:
        return "Nan"

if __name__ == "__main__":
    print(congruence(10, 4, 6))  # True
    print(congruence(10, 5, 3))  # False
    print(congruence(10, 4, 0))  # "Nan"