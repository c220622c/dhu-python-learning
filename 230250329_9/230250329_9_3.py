# 第9次作业 - 水果统计：带可变数量参数的函数
# 230250329 第9章第3节作业

def countSelectedFruit(onefruit, twofruit, *otherfruits):
    """
    带可变数量参数的水果统计函数

    参数:
    - onefruit: 第一种水果的名称 (不可变数量参数)
    - twofruit: 第二种水果的名称 (不可变数量参数)
    - otherfruits: 剩余水果的名称 (可变数量参数)

    返回:
    - 这些水果出现的总次数
    """

    # 构建所有水果的列表
    all_fruits = [onefruit, twofruit] + list(otherfruits)

    # 统计每种水果出现的次数
    fruit_counts = {}
    for fruit in all_fruits:
        fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1

    # 计算总出现次数
    total_occurrences = sum(fruit_counts.values())

    return total_occurrences

# 连续调用三次函数，分别按照不同的参数组合

# 第一次调用：'香蕉','草莓','苹果'
result1 = countSelectedFruit('香蕉', '草莓', '苹果')
print(f"第一次调用结果('香蕉','草莓','苹果'): {result1}")

# 第二次调用：'苹果','梨子','西瓜','芒果'
result2 = countSelectedFruit('苹果', '梨子', '西瓜', '芒果')
print(f"第二次调用结果('苹果','梨子','西瓜','芒果'): {result2}")

# 第三次调用：'草莓','苹果','梨子','西瓜','芒果'
result3 = countSelectedFruit('草莓', '苹果', '梨子', '西瓜', '芒果')
print(f"第三次调用结果('草莓','苹果','梨子','西瓜','芒果'): {result3}")

# 详细分析每次调用的情况
print("\n详细分析:")
print(f"第一次调用: 3种水果，总次数 = {result1}")
print(f"第二次调用: 4种水果，总次数 = {result2}")
print(f"第三次调用: 5种水果，总次数 = {result3}")

# 测试重复水果的情况
print("\n测试重复水果:")
result_duplicate = countSelectedFruit('苹果', '苹果', '梨子', '苹果', '梨子')
print(f"重复水果测试('苹果','苹果','梨子','苹果','梨子'): {result_duplicate}")
print("其中: 苹果出现3次，梨子出现2次，总计5次")
