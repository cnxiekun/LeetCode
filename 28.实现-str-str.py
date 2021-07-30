#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 80/80 cases passed (40 ms)
        # Your runtime beats 76.42 % of python3 submissions
        # Your memory usage beats 29.83 % of python3 submissions (15.2 MB)
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
# @lc code=end

