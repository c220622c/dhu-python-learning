a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
times = a * b
first_num  = a
second_num = b
# make sure x is bigger
def take_remain(x:int,y:int):
    remain = round( x - x // y * y)
    return y , remain
if a < b :
    temp = a
    a = b
    b = temp 
# ensure a is bigger
while b!=0:
    (a,b) = take_remain(a,b)
print(f"{first_num}和{second_num}的最大公约数是{a}，最小公倍数是{int(times/a)}")
