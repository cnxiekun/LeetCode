#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """优化迭代：不需要dp table，记录两个数值就可以了"""
        # 200/200 cases passed (28 ms)
        # Your runtime beats 98.06 % of python3 submissions
        # Your memory usage beats 71.45 % of python3 submissions (15.5 MB)
        dp_i_0, dp_i_1 = 0, -prices[0]
        for price in prices:
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + price), max(dp_i_1, dp_i_0 - price)
        return dp_i_0
# @lc code=end

