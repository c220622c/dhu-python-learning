def issue4():
    x = int(input("请输入年用水量: "))
    if x <= 220:
        cost = x * 3.45
    elif x <= 300:
        cost = 220 * 3.45 + (x - 220) * 4.83
    else:
        cost = 220 * 3.45 + 80 * 4.83 + (x - 300) * 5.83
    print(f"总水费为:{cost}元")


issue4()
