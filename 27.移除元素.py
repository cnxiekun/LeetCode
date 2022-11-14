#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 113/113 cases passed (24 ms)
        # Your runtime beats 98.97 % of python3 submissions
        # Your memory usage beats 16.58 % of python3 submissions (15 MB)
        # res = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[res] = nums[i]
        #         res += 1
        # return res
        if not nums:
            return 0
        
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end

