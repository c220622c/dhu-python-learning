def issue1():
    x = int(input("请输入任意数字: "))
    x_power = x**20
    digits = len(str(abs(x_power)))
    print(f"{x}的20次幂的值为{x_power},位数为{digits}")


issue1()
