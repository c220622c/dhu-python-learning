amount = float(input("请输入二位小数："))
def split_2f(num:float):
    extend = num * 100
    int_part = int(extend // 100)
    remains = extend % 100
    decile_part = int(remains // 10)
    permile_part = round((num - int_part - decile_part / 10 ) * 100)
    print(f"对应人民币为：{int_part}元{decile_part}角{permile_part}分")
split_2f(amount)
# 可以测试2.32 * 100 =
# 231.9999999这种数字，值得注意的是round在3.11后改为了银行家舍入法(当取到0.5时自动取附近的偶数)，不过对于这里为了减少精度的计算还是有用的。
