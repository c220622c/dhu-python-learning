# 纯循环
def pure_loop(n) -> int:
    total = 1
    for i in range(1, n + 1):
        total = total * i
    return total
# 嵌套循环
def nesting_loop(n) -> int:
    if n == 1:
        total = 1
    else:
        total = pure_loop(n-1)*n
    return total
def interface_loop() -> bool:
    num = input("请输入n的值: ")
    if num.isdigit():
        n = int(num)
        result = nesting_loop(n)
        #result = pure_loop(input_integer)
        print(f"{n}!的结果为: {result}")
        return True
    else:
        print("请输入10以内的正整数")
        return False

interface_loop()
