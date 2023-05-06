import random
 
 
def shift_only(la):
    for a in la:
        if a % 2:
            return False
    return True
        
 
if __name__ == "__main__":
    # input parameters
    N:int = int(input())      
    la = input().split()
    la = [int(a) for a in la]
    
    iter = 0
    while shift_only(la):
        iter += 1
        la = [a // 2 for a in la]
 
    print(iter)
