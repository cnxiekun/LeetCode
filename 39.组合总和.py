#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(candidates, track, track_sum, target):
            if track_sum == target:
                res.append(track[:])
                return
            elif track_sum > target:
                return
            for i in range(len(candidates)):
                track.append(candidates[i])
                track_sum += candidates[i]
                backtrack(candidates[i:], track, track_sum, target)
                track.pop()
                track_sum -= candidates[i]

        backtrack(candidates, [], 0, target)
        return res
# @lc code=end

