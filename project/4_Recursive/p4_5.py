import copy
import random
import time


def func(k:int, current:int, flag:int, lc:int):
    # base case
    if current > k: return 
    if (flag == 7): lc[0] += 1

    func(k, current*10 + 7, flag | 4, lc)
    func(k, current*10 + 5, flag | 2, lc)
    func(k, current*10 + 3, flag | 1, lc)


if __name__ == "__main__":
    # input parameters
    K:int = int(input("Input N:"))
    lc:list = [0]
        
    # partial sum
    start_time = time.time()
    func(K, 0, 0, lc)
    print(lc[0])
    print("calculation time:", time.time() - start_time)
