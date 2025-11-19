import random
question_nums = 5
correct_nums = 0
for i in range(question_nums):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    answer = input(f"请计算{a}+{b}=\n请输入您的运算结果：")
    if answer.isdigit():
        answer = int(answer)
        if answer == a+b:
            correct_nums =correct_nums + 1
if correct_nums >= question_nums*0.8:
    print("恭喜！闯关成功！")
else:
    print("抱歉，闯关失败！")