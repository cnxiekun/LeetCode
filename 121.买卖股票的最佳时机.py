#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # """
        # DP table
        # """
        # n = len(prices)
        # dp = [[None, None]] * n
        # for i in range(n):
        #     if i == 0:
        #         dp[0][0] = 0
        #         dp[0][1] = -prices[0]
        #         continue
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #     dp[i][1] = max(dp[i-1][1], -prices[i])
        # return dp[n-1][0]
        """
        简化空间
        """
        dp_i_0, dp_i_1 = 0, -prices[0]
        for p in prices:
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            dp_i_1 = max(dp_i_1, -p)
        return dp_i_0
# @lc code=end

