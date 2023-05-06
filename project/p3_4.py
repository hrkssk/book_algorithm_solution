import random


if __name__ == "__main__":
    # input parameters
    N:int = int(input("Input N:"))
    
    # set list
    la = [random.randint(0,9) for _ in range(N)]
    print("a_i:", la)

    min_value:int = 10
    max_value:int = 0
    for a in la:
        if min_value > a:
            min_value = a
        if max_value < a:
            max_value = a

    print("max_diff:", max_value - min_value)
