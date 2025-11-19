from random import choice
fruits = ["香蕉", "草莓", "苹果",
         "梨子", "西瓜", "芒果",
         "葡萄"]
results = {}
N = 100
for _ in range(N):
    fruit_choice = choice(fruits)
    results[fruit_choice] = results.get(fruit_choice, 0) + 1
for k,v in results.items():
    print(f"{k}出现了{v}次")