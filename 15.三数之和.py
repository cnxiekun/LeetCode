#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 318/318 cases passed (4408 ms)
        # Your runtime beats 9.82 % of python3 submissions
        # Your memory usage beats 8.25 % of python3 submissions (18.6 MB)
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            seen = {}
            target = -nums[i]
            for j in range(i+1, len(nums)):
                remaning = target - nums[j]
                if remaning in seen:
                    # tmp = sorted([nums[i], remaning, nums[j]])
                    tmp = [nums[i], remaning, nums[j]]
                    if tmp not in res:
                        res.append(tmp)
                else:
                    seen[nums[j]] = j
        return res
# @lc code=end

