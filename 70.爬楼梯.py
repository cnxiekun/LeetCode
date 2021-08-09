#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 45/45 cases passed (32 ms)
        # Your runtime beats 82.09 % of python3 submissions
        # Your memory usage beats 33.48 % of python3 submissions (14.9 MB)
        if n <= 2:
            return n
        count = 3
        # 缓存前两次的结果，避免重复计算
        prev_1, prev_2 = 2, 1
        while count <= n:
            res = prev_1 + prev_2
            prev_1, prev_2 = res, prev_1
            count += 1
        return res
# @lc code=end

