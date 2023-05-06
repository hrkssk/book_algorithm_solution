import random


if __name__ == "__main__":
    # input parameters
    N:int = int(input("Input N:"))
    v:int = int(input("Input v:"))
    
    # set list
    la = [random.randint(0,9) for _ in range(N)]
    print("a_i:", la)

    # linear search
    idx:int = None
    for i,a in enumerate(la):
        if a == v:
            idx = i # set index
            break

    print(idx)