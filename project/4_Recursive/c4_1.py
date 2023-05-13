def func(n:int):
    if n==0: return 0
    return n + func(n-1)


if __name__ == "__main__":
    # input parameters
    n = int(input())
    sum = func(n)
    print(sum)