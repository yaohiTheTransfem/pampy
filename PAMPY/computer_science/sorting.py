def bubble_sort(a):
    for ite in range((len(a)-1)):
        if a[ite-1] > a[ite]:
            a[ite-1] = a[ite]
        else:
            pass
    return a

def lee_sort(a):
    numbers = [33, 23, 43, 65, 86, 37 ,65, 39, 65, 37, 32, 74, 74] ## if a > b swap a to b position
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(f"j is {j}")
            if numbers[i] > numbers[j]: 
                pass
            else: numbers[i], numbers[j] = numbers[j], numbers[i]
            print(f"i is {i}") 
            print(f"the list sorted is {numbers}")