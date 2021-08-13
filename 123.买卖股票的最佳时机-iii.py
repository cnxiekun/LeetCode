#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """迭代：DP Table"""
        """
        dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
        dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
        """
        # 214/214 cases passed (352 ms)
        # Your runtime beats 86.32 % of python3 submissions
        # Your memory usage beats 91.38 % of python3 submissions (24.5 MB)
        dp_i20 = dp_i10 = 0
        dp_i21 = dp_i11 = -prices[0]
        for price in prices:
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
            dp_i10 = max(dp_i10, dp_i11 + price)
            dp_i11 = max(dp_i11, - price)
        return dp_i20
# @lc code=end

