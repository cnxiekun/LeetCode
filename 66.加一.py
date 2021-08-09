#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 111/111 cases passed (36 ms)
        # Your runtime beats 71.47 % of python3 submissions
        # Your memory usage beats 7.36 % of python3 submissions (15 MB)
        num = int("".join([str(d) for d in digits])) + 1
        return [int(s) for s in str(num)]
# @lc code=end

