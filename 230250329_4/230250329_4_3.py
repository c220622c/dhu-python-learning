import math
def is_prime(input_integer):
    for divisor in range(2,1+int(math.sqrt(int(input_integer)))):
        if input_integer % divisor == 0:
            return False
    return True
if __name__ == "__main__":
    n = input("请输入一个整数:")
    if not n.lstrip('-').isdigit():
        print("请输入整数")
    else:
        n = int(n)
        if n < 2:
            print(f"{n}不是质数")
        else:
            if is_prime(n):
                print(f"{n}是质数")
            else:
                print(f"{n}不是质数")