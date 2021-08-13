#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """优化迭代：不需要dp table，记录两个数值就可以了"""
        # 211/211 cases passed (244 ms)
        # Your runtime beats 58.81 % of python3 submissions
        # Your memory usage beats 72.13 % of python3 submissions (22.9 MB)
        dp_i_0, dp_i_1 = 0, -prices[0]
        for price in prices:
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, -price)
        return dp_i_0

        # """迭代：DP Table"""
        # # 211/211 cases passed (368 ms)
        # # Your runtime beats 14.52 % of python3 submissions
        # # Your memory usage beats 35.31 % of python3 submissions (23.5 MB)
        # n = len(prices)
        # dp = [[None, None]] * n
        # for i in range(n):
        #     if i == 0:
        #         dp[0][0] = 0
        #         dp[0][1] = -prices[0]
        #         continue
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #     dp[i][1] = max(dp[i-1][1], - prices[i])
        # return dp[n-1][0]
# @lc code=end

