def issue2(weight, height) -> float:
    return weight / (height**2)


weight = input("请输入体重(kg): ")
height = input("请输入身高(m): ")
bmi = issue2(float(weight), float(height))
print("BMI值为: %.1f" % bmi)
