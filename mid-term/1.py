#! wzj 2026.1.16
a = int(input("请输入a的值："))
b = int(input("请输入b的值，不为0:"))
c = a / b
num = 3
# 函数化写法，将数字写成文字需要用第三方库，这次就不转换了
"""
for i in range(num):
    seperator = '=' * (num-i)
    print(f"{a}/{b}保留{i+1}位小数的结果为:{seperator}{c:.{i+1}f}")
"""
# 简单写法
print(f"{a}/{b}保留一位小数的结果为:{'='*3}{c:.1f}")
print(f"{a}/{b}保留二位小数的结果为:{'='*2}{c:.2f}")
print(f"{a}/{b}保留三位小数的结果为:{'='*1}{c:.3f}")
# f字符串是python3.6加入的特性  我认为比format方便
name = "Jack Weng"
print(f"I'm {name}")
print("I'm {}".format(name))
print("I'm {who}".format(who=name))
