#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 46/46 cases passed (32 ms)
        # Your runtime beats 96.15 % of python3 submissions
        # Your memory usage beats 18.32 % of python3 submissions (15.9 MB)
        l, r = 0, len(nums) - 1
        while l <= r:
            med = (l + r) // 2
            if nums[med] == target:
                return med
            if nums[med] > target:
                r = med - 1
            else:
                l = med + 1
        return -1
# @lc code=end

