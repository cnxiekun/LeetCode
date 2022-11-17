#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, track = [], []

        def backtrack(nums, depth):
            res.append(track[:])
            for i in range(depth, len(nums)):
                # 已回溯过得相同值节点，就跳过
                if i > depth and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                backtrack(nums, i + 1)
                track.pop()
        
        backtrack(nums, 0)
        return res
# @lc code=end

