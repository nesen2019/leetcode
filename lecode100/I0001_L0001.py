"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
通过次数1,646,513提交次数3,314,328

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

    @staticmethod
    def check_class(solution=None):
        if solution is None:
            solution = Solution
        assert solution().twoSum(nums=[2, 7, 11, 15], target=9) in [[0, 1], [1, 0]], solution
        assert solution().twoSum(nums=[3, 2, 4], target=6) in [[1, 2], [2, 1]], solution

    def check_func(self, func=None):
        if func is None:
            func = self.twoSum
        assert func(nums=[2, 7, 11, 15], target=9) in [[0, 1], [1, 0]], func
        assert func(nums=[3, 2, 4], target=6) in [[1, 2], [2, 1]], func


if __name__ == '__main__':
    # Solution.check_class()
    c = Solution()
    c.check_func(func=c.twoSum)
