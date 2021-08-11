#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """DP: 自底向上"""
        # 188/188 cases passed (1004 ms)
        # Your runtime beats 86.1 % of python3 submissions
        # Your memory usage beats 50.8 % of python3 submissions (15.2 MB)
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])
        return dp[amount] if dp[amount] != amount + 1 else -1
# @lc code=end

