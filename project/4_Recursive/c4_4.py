def GCD(m:int, n:int):
    if n==0: return m
    return GCD(n, m%n)

if __name__ == "__main__":
    print(GCD(51,15))
    print(GCD(15,51))