#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP 自底向上
        """
        n = len(nums)
        dp_i_0, dp_i_1, dp_i_2 = 0, 0, 0
        for i in range(n-1, -1, -1):
            dp_i_0 = max(dp_i_1, dp_i_2 + nums[i])
            dp_i_1, dp_i_2 = dp_i_0, dp_i_1
        return dp_i_0
# @lc code=end

