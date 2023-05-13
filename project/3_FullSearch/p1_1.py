
def binary_search(limit:int, age:int, start_range:int, stop_range:int):
    threshold = (start_range + stop_range) // 2
    for _ in range(limit):
        print(f"あなた：{threshold}未満ですか？")
        if age < threshold:
            print("Aさん：YES")
            stop_range = threshold
            threshold = (start_range + stop_range) // 2
        else:
            print("Aさん：NO")
            start_range = threshold
            threshold = (start_range + stop_range) // 2
        
        if start_range == threshold:
            return threshold

    if age == threshold+1:
        return threshold+1
    
    return None

if __name__ == "__main__":
    age = int(input(f"Aさんの年齢を入力してください"))
    answer = binary_search(limit = 4, age=age, start_range=20, stop_range=36)
    if answer:
        print(f"あなた：Aさんは{answer}歳です。")
    else:
        print("Aさんの年齢を絞りこめませんでした。")

    


