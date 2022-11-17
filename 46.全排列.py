#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯算法 DFS Depth-First-Search
        for 选择 in 选择列表:
            # 做选择
            将该选择从选择列表移除
            路径.add(选择)
            backtrack(路径, 选择列表)
            # 撤销选择
            路径.remove(选择)
            将该选择再加入选择列表
        """
        def backtrack(res, track, choice):
            """
            res: 返回的结果
            track: 当前路径，初始化是[]
            choice: 路径可选集合
            """
            # 判断当前结果是否以满足条件
            if len(track) == len(choice):
                """必须用track[:]，否则track是空列表[]"""
                # print(track)
                res.append(track[:])
            # 做选择
            for c in choice:
                # 判断当前选择是否已被使用：是否已在路径中(不合理的选择)
                if c in track:
                    continue

                track.append(c)
                backtrack(res, track, choice)
                track.pop()
        
        res = []
        backtrack(res, [], nums)
        return res
# @lc code=end

