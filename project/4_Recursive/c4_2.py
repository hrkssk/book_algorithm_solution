def func(n:int):
    print(f"func({n})を呼び出しました")
    if n==0: return 0
    result = n + func(n-1)
    print(f"{n}までの総和 = {result}")
    return result

if __name__ == "__main__":
    func(5)