import copy
import random
import time


def func(i:int, w:int, la:list):
    # base case
    if i == 0:
        if w == 0: return True
        else: return False
    
    if func(i-1, w, la): return True
    if func(i-1, w-la[i-1], la): return True
    return False


if __name__ == "__main__":
    # input parameters
#    N:int = int(input("Input N:"))
#    W:int = int(input("Input W:"))
    
    # set list
#    la:int = [random.randint(0,9) for _ in range(N)]
#    print("a_i:", la)

    N:int = 5
    W:int = 10
    la = [1,2,4,5,11]    #test1
#    la = [1,5,8,11]    #test2

    # partial sum
    start_time = time.time()
    if func(N, W, la):
        print("Yes")
    else:
        print("No")
    print("calculation time:", time.time() - start_time)
