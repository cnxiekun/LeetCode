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
        res = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1
        return res
# @lc code=end

