#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 11510/11510 cases passed (60 ms)
        # Your runtime beats 87.37 % of python3 submissions
        # Your memory usage beats 55.6 % of python3 submissions (14.9 MB)
        return str(x) == str(x)[::-1]
# @lc code=end

