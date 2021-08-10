#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 88/88 cases passed (28 ms)
        # Your runtime beats 95.24 % of python3 submissions
        # Your memory usage beats 6.06 % of python3 submissions (15.8 MB)
        l, r = 0, len(nums) - 1
        while l <= r:
            med = (l + r) // 2
            if nums[med] < target:
                l = med + 1
            elif nums[med] > target:
                r = med - 1
            else:
                while nums[l] != target:
                    l += 1
                while nums[r] != target:
                    r -= 1
                return [l, r]
        return [-1, -1]
# @lc code=end

