#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # 1032/1032 cases passed (32 ms)
        # Your runtime beats 92.87 % of python3 submissions
        # Your memory usage beats 16.12 % of python3 submissions (15 MB)
        if x >= 0:
            res =  int(str(x)[::-1])
        else:
            res = -int(str(-x)[::-1])
        if res >= 2 ** 31 or res < -2**31:
            return 0
        return res
# @lc code=end

