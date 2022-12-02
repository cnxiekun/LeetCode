#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.binarySearchLeft(nums, target), self.binarySearchRight(nums, target)
        return [left, right] if left <= right else [-1, -1]
    
    
    def binarySearchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            med = (left + right) // 2
            if nums[med] >= target:
                right -= 1
            else:
                left += 1
        return left

    
    def binarySearchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            med = (left + right) // 2
            if nums[med] <= target:
                left += 1
            else:
                right -= 1
        return right
# @lc code=end

