if __name__ == "__main__":
    # input parameters
    la = [int(a) for a in input()]
    la.reverse()

    sum:int = 0
    N:int = len(la) - 1
    for iter in range(2**N):
        count = 0
        _sum = la[0]
        for bit in range(N):
            if (iter & 2**bit):
                count = 0
            else:
                count += 1
            _sum += la[bit+1] * 10**count
#        print(f"iter, _sum: {iter:04b}, {_sum}")
        sum += _sum

    print(sum)
