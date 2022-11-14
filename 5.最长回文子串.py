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
        # length = len(s)
        # if length <= 1:
        #     return s
        # dp = [[0] * length for _ in range(length)]
        # max_len = 1
        # start = end = 0
        # for j in range(length):
        #     for i in range(j):
        #         if i == j - 1:
        #             dp[i][j] = s[i] == s[j]
        #         else:
        #             dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        #         if dp[i][j] and max_len < j - i + 1:
        #             max_len = j - i + 1
        #             start = i
        #             end = j
        #     dp[j][j] = 1
        # return s[start:end+1]
        def palindrome(s, i, j):
            """
            返回以s[i], s[j]为中心的回文子串
            一般 j=i or j=i+1
            """
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        res = ""
        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i + 1)
            res = res if len(s1) < len(res) else s1
            res = res if len(s2) < len(res) else s2
        return res
# @lc code=end

