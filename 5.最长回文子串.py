#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        DP进阶版，固定首尾
        """
        # 177/177 cases passed (6384 ms)
        # Your runtime beats 40.99 % of python3 submissions
        # Your memory usage beats 46.78 % of python3 submissions (22.3 MB)
        length = len(s)
        if length <= 1:
            return s
        dp = [[0] * length for _ in range(length)]
        max_len = 1
        start = end = 0
        for j in range(length):
            for i in range(j):
                if i == j - 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                if dp[i][j] and max_len < j - i + 1:
                    max_len = j - i + 1
                    start = i
                    end = j
            dp[j][j] = 1
        return s[start:end+1]


# @lc code=end

