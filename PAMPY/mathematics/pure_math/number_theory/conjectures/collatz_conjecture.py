def collatz_conjecture(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n*3)+1
        steps += 1
    return steps

for ite in range(1, 10000000):
    print(f"The number of steps to do {ite} is {collatz_conjecture(ite)}")
