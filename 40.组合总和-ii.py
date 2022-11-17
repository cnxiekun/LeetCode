#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(candidates, depth, track, track_sum, target):
            if track_sum == target:
                res.append(track[:])
                return
            elif track_sum > target:
                return
            for i in range(depth, len(candidates)):
                if i > depth and candidates[i] == candidates[i-1]:
                    continue
                track.append(candidates[i])
                track_sum += candidates[i]
                backtrack(candidates, i + 1, track, track_sum, target)
                track.pop()
                track_sum -= candidates[i]

        backtrack(candidates, 0, [], 0, target)
        return res
# @lc code=end

