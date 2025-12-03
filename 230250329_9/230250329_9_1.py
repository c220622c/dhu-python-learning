from random import choice
def CountApple() -> int:
    fruits = ["香蕉", "草莓", "苹果",
         "梨子", "西瓜", "芒果",
         "葡萄"]
    results = {}
    N = 100
    for _ in range(N):
        fruit_choice = choice(fruits)
        results[fruit_choice] = results.get(fruit_choice, 0) + 1
    return results["苹果"]
for i in range(3):
    print(f"第{i+1}次得到{CountApple()}个苹果")
