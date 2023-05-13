import random


if __name__ == "__main__":
    # input parameters
    N:int = int(input("Input N:"))
    K:int = int(input("Input K:"))
    
    # set list
    la:int = [random.randint(0,9) for _ in range(N)]
    lb:int = [random.randint(0,9) for _ in range(N)]
    print("a_i:", la)
    print("b_i:", lb)

    # linear search
    min_value:float = float('inf')
    for a in la:
        for b in lb:
            ab = a + b
            if (K < ab) and (ab < min_value):
                min_value = ab # update min_value

    print(min_value)