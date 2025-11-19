def issue2(a: str, n: int):
    b = a.split(",")
    for i in range(len(b)):
        print(f"第{i + 1}个参数是:{b[i]}")
    joined_chars = ",".join(b[0:n])
    print(f"前{n}个参数分别是:{joined_chars}")


issue2(input("请输入大于3个的参数并用英文逗号连接: "), 3)
