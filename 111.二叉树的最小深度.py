#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """DFS 深度优先搜索 -- 递归"""
        # 52/52 cases passed (488 ms)
        # Your runtime beats 75.21 % of python3 submissions
        # Your memory usage beats 59.25 % of python3 submissions (54.4 MB)
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        # """BFS 广义优先搜索 -- 迭代"""
        # # 52/52 cases passed (436 ms)
        # # Your runtime beats 90.26 % of python3 submissions
        # # Your memory usage beats 98.45 % of python3 submissions (50.5 MB)
        # if not root:
        #     return 0
        # depth = 1
        # queue = [[root]]
        # while queue:
        #     q = queue.pop()
        #     tmp = []  # 存储下一层要遍历的所有节点
        #     for node in q:
        #         # 当前层若是某节点已经是根节点，这最小深度已经达到
        #         if not node.left and not node.right:
        #             return depth
        #         # 否则下次还需遍历其子节点
        #         if node.left:
        #             tmp.append(node.left)
        #         if node.right:
        #             tmp.append(node.right)
        #     queue.append(tmp)
        #     depth += 1
# @lc code=end

