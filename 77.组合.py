#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, track = [], []

        def backtrack(n, depth):
            # track 表示当前路径
            if len(track) == k:
                # print(track)
                res.append(track[:])
                return

            for i in range(depth, n+1):
                # 选择i
                track.append(i)
                backtrack(n, i + 1)
                # 撤销选择
                track.pop()
        
        backtrack(n, 1)
        return res
# @lc code=end

