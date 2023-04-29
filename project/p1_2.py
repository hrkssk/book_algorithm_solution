def binary_search(limit:int, age:int, start_range:int, stop_range:int):
    threshold = (start_range + stop_range) // 2
    for _ in range(limit):
        #print(f"あなた：{threshold}未満ですか？")
        if age < threshold:
            #print("Aさん：YES")
            stop_range = threshold
            threshold = (start_range + stop_range) // 2
        else:
            #print("Aさん：NO")
            start_range = threshold
            threshold = (start_range + stop_range) // 2
        
        if start_range == threshold:
            return threshold

    if age == threshold+1:
        return threshold+1
    
    return None

def age_quiz(limit:int, start_range:int, stop_range:int):
    for age in range(start_range, stop_range):
        answer = binary_search(limit=limit, age=age, start_range=start_range, stop_range=stop_range)
        if answer is None:
            print(f"{limit}回の質問では、{age}歳の場合、年齢をあてることができません。")
            return False
    return True

def need_to_ask(limit:int, start_range:int, stop_range:int):
    for iter in range(limit):
        if age_quiz(limit=iter+1, start_range=start_range, stop_range=stop_range):
            print(f"{iter+1}回の質問で、Aさんの年齢が確実にわかります。")
            return True
    print(f"{limit}回の質問で、Aさんの年齢を確実に当てることはできません。")
    return False


if __name__ == "__main__":
    need_to_ask(limit=7, start_range=0, stop_range=100)
