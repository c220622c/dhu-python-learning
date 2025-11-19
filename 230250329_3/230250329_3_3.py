def issue3():
    x = int(input("请输入年份值: "))
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print("是闰年")
    else:
        print("不是闰年")
    return True


issue3()
