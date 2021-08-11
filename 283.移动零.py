#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 21/21 cases passed (36 ms)
        # Your runtime beats 77.1 % of python3 submissions
        # Your memory usage beats 10.62 % of python3 submissions (15.4 MB)
        zero = 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums
        # # 21/21 cases passed (28 ms)
        # # Your runtime beats 96.4 % of python3 submissions
        # # Your memory usage beats 22.09 % of python3 submissions (15.3 MB)
        # if len(nums) <= 1:
        #     return nums
        # p1 = p2 = 0
        # while p2 < len(nums):
        #     while p2 < len(nums) and nums[p2] == 0:
        #         p2 += 1
        #     if p2 == len(nums):
        #         return nums
        #     nums[p1], nums[p2] = nums[p2], nums[p1]
        #     p1 += 1
        #     p2 += 1
        # return nums
# @lc code=end

