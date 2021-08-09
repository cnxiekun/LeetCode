#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 1017/1017 cases passed (76 ms)
        # Your runtime beats 13.14 % of python3 submissions
        # Your memory usage beats 43.15 % of python3 submissions (14.9 MB)
        if x <= 1:
            return x
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            if (mid - 1) ** 2 <= x < mid ** 2:
                return mid - 1
            elif x > mid ** 2:
                left = mid + 1
            else:
                right = mid - 1
# @lc code=end

