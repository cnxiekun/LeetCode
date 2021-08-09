#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """亦或算法"""
        # 61/61 cases passed (44 ms)
        # Your runtime beats 77.44 % of python3 submissions
        # Your memory usage beats 21.27 % of python3 submissions (16.6 MB)
        for num in nums[1:]:
            nums[0] ^= num
        return nums[0]

        # 61/61 cases passed (40 ms)
        # Your runtime beats 88.56 % of python3 submissions
        # Your memory usage beats 13.75 % of python3 submissions (16.7 MB)
        # seen = {}
        # for num in nums:
        #     if num in seen:
        #         seen.pop(num)
        #     else:
        #         seen[num] = 1
        # return list(seen.keys())[0]
# @lc code=end

