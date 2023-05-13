
def fibo(n:int, memo:list):
    if n==0:
        memo[n] = 0
        return memo[n]
    elif n==1:
        memo[n] = 1
        return memo[n]
    
    if memo[n] != -1: return memo[n]

    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]


if __name__ == "__main__":
    n:int = 50
    memo = [-1 for _ in range(n)]
    fibo(n-1, memo)
    for i in range(n):
        print(f"{i} 項目: {memo[i]}")