#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 58/58 cases passed (24 ms)
        # Your runtime beats 98.67 % of python3 submissions
        # Your memory usage beats 8.13 % of python3 submissions (15.1 MB)
        s = s.split(" ")
        s = [i for i in s if i]
        if not s:
            return 0
        return len(s[-1])
# @lc code=end

