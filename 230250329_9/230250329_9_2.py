from random import choice
def CountFruit(onefruit) -> int:
    fruits = ["香蕉", "草莓", "苹果",
         "梨子", "西瓜", "芒果",
         "葡萄"]
    results = {}
    N = 100
    for _ in range(N):
        fruit_choice = choice(fruits)
        results[fruit_choice] = results.get(fruit_choice, 0) + 1
    return results[onefruit]
print(f"第1次得到{CountFruit("香蕉")}个香蕉")
print(f"第2次得到{CountFruit("草莓")}个草莓")
print(f"第3次得到{CountFruit("苹果")}个苹果")
