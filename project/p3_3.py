import random


def rand_list(N):
    la = []
    while len(la) < N:
        a = random.randint(0,9)
        if not a in la:
            la.append(a)
            
    return la

if __name__ == "__main__":
    # input parameters
    N:int = int(input("Input N:"))
    
    # set list
    la = rand_list(N)
    print("a_i:", la)

    min_value:int = 10
    second_min_value:int = 10
    for a in la:
        if second_min_value > a:
            second_min_value = a
            if min_value > a:
                second_min_value = min_value
                min_value = a
    
    print("second_min_value:", second_min_value)
