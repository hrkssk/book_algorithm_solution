
def tribo(n:int, memo:list):
    if n==0:
        memo[n] = 0
        return memo[n]
    elif n==1:
        memo[n] = 0
        return memo[n]
    elif n==2:
        memo[n] = 1
        return memo[n]
    
    if memo[n] != -1: return memo[n]

    memo[n] = tribo(n-1, memo) + tribo(n-2, memo) + tribo(n-3, memo)
    return memo[n]


if __name__ == "__main__":
    n:int = 10
    memo = [-1 for _ in range(n)]
    tribo(n-1, memo)
    for i in range(n):
        print(f"{i} 項目: {memo[i]}")