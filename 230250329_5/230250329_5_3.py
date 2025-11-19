
def issue3():
    score = [55, 53, 9, 86, 78, 27, 97, 93, 28, 37]
    print(f"score列表为: {score}")
    print(f"score列表元素个数为{len(score)}")
    print(f"第三个元素为{score[2]}")
    print(f"第一到六个元素的值为{score[:6:]}")
    score.insert(3,27)
    score.append(59)
    print(f"添加数据后列表为: {score}")
    del score[0]
    score.pop(-1)
    print(f"删除数据后列表为: {score}")
    print(f"27出现的次数为{score.count(27)}")
    if 86 in score:
        print("86在score列表中")
    score.sort()
    print(f"从小到大排序结果为{score}")
    print(f"调用min和max函数后，得到最大和最小值分别为{min(score)},{max(score)}")
    score.reverse()
    print(f"调用reverse函数后列表为{score}")
    print(f"86的序号为{score.index(86)}")
issue3()
