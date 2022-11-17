#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, track = [], []

        def backtrack(nums, depth):
            # track 表示当前路径
            # print(track)
            res.append(track[:])
            for i in range(depth, len(nums)):
                # 选择nums[i]
                track.append(nums[i])
                backtrack(nums, i + 1)
                # 撤销选择
                track.pop()
        
        backtrack(nums, 0)
        return res
# @lc code=end

