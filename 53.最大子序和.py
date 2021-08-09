#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 203/203 cases passed (40 ms)
        # Your runtime beats 78.75 % of python3 submissions
        # Your memory usage beats 40.11 % of python3 submissions (15.4 MB)
        res = curr = nums[0]
        for num in nums[1:]:
            curr = max(num, curr + num)
            res = max(res, curr)
        return res
# @lc code=end

