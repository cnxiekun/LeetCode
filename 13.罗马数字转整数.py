#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # 3999/3999 cases passed (40 ms)
        # Your runtime beats 97.24 % of python3 submissions
        # Your memory usage beats 71.67 % of python3 submissions (14.9 MB)
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500, "M":1000}
        res = 0
        pos = 0
        while pos < len(s) - 1:
            if d[s[pos]] >= d[s[pos+1]]:
                res += d[s[pos]]
                pos += 1
            else:
                res += d[s[pos+1]]
                res -= d[s[pos]]
                pos += 2
        if pos == len(s) - 1:
            res += d[s[pos]]
        return res
        


# @lc code=end

