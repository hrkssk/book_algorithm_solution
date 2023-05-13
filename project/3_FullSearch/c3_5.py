import random


if __name__ == "__main__":
    # input parameters
    N:int = random.randint(0,1024)

    i:int = 4
    if (N & 2**i):
        print("YES")
    else:
        print("NO")
    
    print('bin: {:10b}'.format(N))
    print('bin: {:10b}'.format(2**i))
