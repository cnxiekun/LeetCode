#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 987/987 cases passed (48 ms)
        # Your runtime beats 97.26 % of python3 submissions
        # Your memory usage beats 98.88 % of python3 submissions (14.7 MB)
        if len(s) <= 1:
            return len(s)
        res = 1
        curr = prev = s[0]
        for char in s[1:]:
            if char in prev:
                curr = prev[prev.index(char) + 1:] + char
            else:
                curr = prev + char
            res = max(res, len(curr))
            prev = curr
        return res
# @lc code=end

