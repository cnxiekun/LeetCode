#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        """DP:自底向上"""
        # 31/31 cases passed (28 ms)
        # Your runtime beats 91.1 % of python3 submissions
        # Your memory usage beats 17.92 % of python3 submissions (15 MB)
        if n <= 1:
            return n
        pre, curr = 0, 1
        for _ in range(n-1):
            res = pre + curr
            pre, curr = curr, res
        return res
        # """DP: 自顶向下"""
        # # 31/31 cases passed (1172 ms)
        # # Your runtime beats 5.28 % of python3 submissions
        # # Your memory usage beats 5.13 % of python3 submissions (15.1 MB)
        # if n <= 1:
        #     return n
        # seen = {0: 0, 1: 1}
        # if n-1 not in seen and n-2 not in seen:
        #     seen[n-2] = self.fib(n-2)
        #     seen[n-1] = self.fib(n-1)
        # elif n-1 not in seen and n-2 in seen:
        #     seen[n-1] = self.fib(n-1)
        # return seen[n-1] + seen[n-2]    
# @lc code=end

