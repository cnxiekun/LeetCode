# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划

# 第三题的***进阶版DP*** 题目三：`固定尾部`的DP，该题目`固定首尾`的DP
# 维护一个二维数组dp，其中dp[j][i]表示字符串区间[j, i]是否为回文串
# 当i = j时，只有一个字符，肯定是回文串
# 如果i = j + 1，说明是相邻字符，此时需要判断s[i]是否等于s[j]
# 如果i和j不相邻，即i - j >= 2时，除了判断s[i]和s[j]相等之外，dp[j + 1][i - 1]若为真，就是回文串
# 比较所有dp[j][i]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        start, end, max_len = 0, 0, 0
        # 初始化dp[j][i]为0：start为j，end为i
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[i] == s[j]) and ((i - j < 2) or dp[j+1][i-1])
                if dp[j][i] == 1 and max_len < i - j + 1:
                    max_len = i - j + 1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start: end + 1]
# leetcode submit region end(Prohibit modification and deletion)
