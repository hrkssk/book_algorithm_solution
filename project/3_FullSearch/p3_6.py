if __name__ == "__main__":
    # input parameters
    la = input().split()
    k, s = [int(a) for a in la]
    _k = min(k, s)
    
    count = 0
    for x in range(_k+1):
        sx = s - x
        for y in range(_k+1):
            sy = sx - y
            if (0 <= sy) and (sy <= k):
                count += 1
#                print("x,y,z:", x, ",", y, ",", sy)
    
    print(count)                
