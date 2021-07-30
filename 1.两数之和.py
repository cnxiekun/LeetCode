#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 54/54 cases passed (28 ms)
        # Your runtime beats 98.45 % of python3 submissions
        # Your memory usage beats 10.12 % of python3 submissions (15.9 MB)
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[v] = i
        return "No solution found"
        # 54/54 cases passed (3072 ms)
        # Your runtime beats 23.69 % of python3 submissions
        # Your memory usage beats 70.87 % of python3 submissions (15 MB)
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return "No solution found"
# @lc code=end

