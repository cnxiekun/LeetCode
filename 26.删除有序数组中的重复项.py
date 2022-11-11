#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 362/362 cases passed (40 ms)
        # Your runtime beats 84.32 % of python3 submissions
        # Your memory usage beats 98.28 % of python3 submissions (15.4 MB)
        # res = 1
        # for i in range(len(nums) - 1):
        #     if nums[i] != nums[i+1]:
        #         nums[res] = nums[i+1]
        #         res += 1
        # nums = nums[:res]
        # return res
        if not nums:
            return 0
        
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1 
# @lc code=end

