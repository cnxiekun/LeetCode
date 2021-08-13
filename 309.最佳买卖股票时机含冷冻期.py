#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """优化迭代：不需要dp table，记录三个数值就可以了"""
        # 210/210 cases passed (32 ms)
        # Your runtime beats 89.89 % of python3 submissions
        # Your memory usage beats 70.68 % of python3 submissions (15.1 MB)
        dp_pre_0, dp_i_0, dp_i_1 = 0, 0, -prices[0]
        for price in prices:
            dp_pre_0, dp_i_0, dp_i_1 = dp_i_0, max(dp_i_0, dp_i_1 + price), max(dp_i_1, dp_pre_0 - price)
        return dp_i_0
# @lc code=end

