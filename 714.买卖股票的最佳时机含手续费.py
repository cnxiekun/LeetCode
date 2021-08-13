#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """优化迭代：不需要dp table，记录两个数值就可以了"""
        # 44/44 cases passed (156 ms)
        # Your runtime beats 86.38 % of python3 submissions
        # Your memory usage beats 74.65 % of python3 submissions (19.8 MB)
        dp_i_0, dp_i_1 = 0, -prices[0]-fee
        for price in prices:
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + price), max(dp_i_1, dp_i_0 - price - fee)
        return dp_i_0
# @lc code=end

