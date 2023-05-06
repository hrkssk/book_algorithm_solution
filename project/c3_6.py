import random
import time


def partial_bit(W, la):
    N:int = len(la)
    sum:int = 0
    for i in range(2**(N)):
        for j in range(N-1):
            if (i & 2**j):
                sum += la[j]
        if sum == W:
            print("*****")
            print('bin: {:4b}'.format(i))
            return True
        else:
            sum = 0
        print('bin: {:4b}'.format(i))
    
    return False

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
    if partial_bit(W, la):
        print("Yes")
    else:
        print("No")
    print("calculation time:", time.time() - start_time)
