import copy
import random
import time


def partial(W:int, la:list):
    
    for a in la:
        _W = W - a
        if _W == 0:
            return True
        elif _W < 0:
            return False
        else:
            _la = copy.deepcopy(la)
            _la.remove(a)
            if partial(_W, _la):
                return True


if __name__ == "__main__":
    # input parameters
#    N:int = int(input("Input N:"))
#    W:int = int(input("Input W:"))
    
    # set list
#    la:int = [random.randint(0,9) for _ in range(N)]
#    print("a_i:", la)

    W:int = 10
    la = [1,2,4,5,11]    #test1
#    la = [1,5,8,11]    #test2

    # partial sum
    start_time = time.time()
    if partial(W, la):
        print("Yes")
    else:
        print("No")
    print("calculation time:", time.time() - start_time)
