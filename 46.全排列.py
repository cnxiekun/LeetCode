#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """回溯算法: DFS Depth-First-Search"""
        # 26/26 cases passed (32 ms)
        # Your runtime beats 88.31 % of python3 submissions
        # Your memory usage beats 45.62 % of python3 submissions (15.1 MB)
        res = []
        self.backtrack(res, [], nums)
        return res

    def backtrack(self, res, track, choice):
        if len(track) == len(choice):
            """必须用track[:]，否则track是空列表[]"""
            res.append(track[:])
        for c in choice:
            # 排除不合理的选择
            if c in track:
                continue
            # 做选择
            track.append(c)
            # 进入下一步决策树
            self.backtrack(res, track, choice)
            # 撤销选择
            track.pop()

# @lc code=end

