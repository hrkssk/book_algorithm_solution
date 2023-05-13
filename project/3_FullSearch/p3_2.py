import random


if __name__ == "__main__":
    # input parameters
    N:int = int(input("Input N:"))
    v:int = int(input("Input v:"))
    
    # set list
    la = [random.randint(0,9) for _ in range(N)]
    print("a_i:", la)

    count:int = 0
    for a in la:
        if v == a:
            count += 1
    
    print("count:", count)
