#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.robRange(nums, 0, n - 2), self.robRange(nums, 1, n - 1))
    
    def robRange(self, nums, start, end):
        """
        dp 返回[start,end]区间的最大值
        """
        dp_i_0, dp_i_1, dp_i_2 = 0, 0, 0
        for i in range(end, start - 1, -1):
            dp_i_0 = max(dp_i_1, dp_i_2 + nums[i])
            dp_i_1, dp_i_2 = dp_i_0, dp_i_1
        return dp_i_0
# @lc code=end

