from random import choice
def countSelectedFruit(onefruit, twofruit, *otherfruits):
    fruits = ["香蕉", "草莓", "苹果", "梨子", "西瓜", "芒果", "葡萄"]
    results = {}
    output_list = {}
    N = 100
    fruit_output_list = [onefruit, twofruit]
    for other_fruit in otherfruits:
        fruit_output_list.append(other_fruit)
    for _ in range(N):
        fruit_choice = choice(fruits)
        results[fruit_choice] = results.get(fruit_choice, 0) + 1
    for output_fruit in fruit_output_list:
        # print(output_fruit)
        output_list[output_fruit] = results[output_fruit]
    sum = 0
    for output_fruit in output_list:
        sum = sum + output_list[output_fruit]
    return sum
# countSelectedFruit("香蕉","苹果")
args_list = [
    ["香蕉", "草莓", "苹果"],
    ["苹果", "梨子", "西瓜", "芒果"],
    ["草莓", "苹果", "梨子", "西瓜", "芒果"],
]

# 使用args_list作为函数参数传入
"""
if __name__ == "__main__":
    for i in range(len(args_list)):
        print(
            f"第{i+1}次共得到{countSelectedFruit(args_list[i][0],args_list[i][1],*args_list[i])}个{",".join(args_list[i])}。"
        )
"""

for i in range(len(args_list)):
    print(
        f"第{i+1}次共得到{countSelectedFruit(args_list[i][0],args_list[i][1],*args_list[i])}个{",".join(args_list[i])}。"
    )
