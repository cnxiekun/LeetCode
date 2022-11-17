#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, n = [], len(nums)

        def backtrack(nums, track):
            if len(track) == n:
                res.append(track[:])
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                backtrack(nums[:i] + nums[i+1:], track)
                track.pop()
        
        backtrack(nums, [])
        return res
# @lc code=end

