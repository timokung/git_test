def add(a, b):
    """簡單加法函式"""
    return a + b

if __name__ == "__main__":
    # 測試 greet 函式
    name = input("請輸入你的名字: ")
    print(greet(name))

    # 測試 add 函式
    print("3 + 5 =", add(3, 5))