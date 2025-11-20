def issue1():
    s = input("请输入字符串: ")
    result = ""
    for char in s:
        if char not in result:
            result += char
    
    print("去重后的结果为:", result)
issue1()
