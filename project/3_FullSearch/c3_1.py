import random


if __name__ == "__main__":
    # input parameters
    N:int = int(input("Input N:"))
    v:int = int(input("Input v:"))
    
    # set list
    la = [random.randint(0,9) for _ in range(N)]
    print("a_i:", la)

    # linear search
    exist:bool = False   # init flag
    for a in la:
        if a == v:
            exist = True # change flag

    if exist:
        print(f"Yes")
    else:
        print(f"No")

