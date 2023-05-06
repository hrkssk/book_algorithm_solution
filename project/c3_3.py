import random


if __name__ == "__main__":
    # input parameters
    N:int = int(input("Input N:"))
    
    # set list
    la = [random.randint(0,9) for _ in range(N)]
    print("a_i:", la)

    # linear search
    min_value:float = float('inf')
    for a in la:
        if a < min_value:
            min_value = a # update min_value

    print(min_value)