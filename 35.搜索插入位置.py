#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 62/62 cases passed (32 ms)
        # Your runtime beats 85.42 % of python3 submissions
        # Your memory usage beats 5.16 % of python3 submissions (15.6 MB)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
        return left
# @lc code=end

