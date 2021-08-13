#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """DP table: 最多进行k次交易"""
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0, -float("inf")]] * (k+1)] * n
        for i in range(n):
            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[n-1][k][0]
# @lc code=end

