"""
这里我们引用leetcode的python第一题来做一个例子
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
示例 1：
 输入：nums = [2,7,11,15], target = 9
 输出：[0,1]
 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
 输入：nums = [3,2,4], target = 6
 输出：[1,2]
"""
# 双层循环方法
class SolutionBruteForce(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# hashmap方法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache_map = {}
        for i, num in enumerate(nums):
            complement = target - nums[i]
            if complement in cache_map:
                return [cache_map[complement], i]
            cache_map[num] = i
        return []


# 性能对比测试
if __name__ == "__main__":
    import time
    import random
    
    # 创建测试数据
    test_sizes = [100, 500, 1000, 2000, 5000]
    runs = 100  # 运行多次取平均值
    
    # 打印表头
    print("\n" + "-" * 70)
    print(f"{'数组大小':^10} | {'双层循环(ms)':>15} | {'HashMap(ms)':>15} | {'速度比':>10}")
    print("-" * 70)
    
    for size in test_sizes:
        brute_total = 0
        hash_total = 0
        
        # 运行多次取平均
        for _ in range(runs):
            # 生成随机数组
            nums = random.sample(range(size * 10), size)
            # 生成答案
            target = nums[-2] + nums[-1]  # 使用后两个元素作为目标
            
            # 测试双层循环方法
            solution_brute = SolutionBruteForce()
            start_time = time.perf_counter()
            result1 = solution_brute.twoSum(nums, target)
            brute_total += time.perf_counter() - start_time
            
            # 测试 HashMap 方法
            solution_hash = Solution()
            start_time = time.perf_counter()
            result2 = solution_hash.twoSum(nums, target)
            hash_total += time.perf_counter() - start_time
        
        # 计算平均时间
        brute_avg = brute_total / runs * 1000  # 转换为毫秒
        hash_avg = hash_total / runs * 1000    # 转换为毫秒
        ratio = brute_avg / hash_avg if hash_avg > 0 else 0
        
        print(f"{size:^12} | {brute_avg:>18.4f} | {hash_avg:>15.4f} | {ratio:>9.2f}x")
    
    print("-" * 70)
