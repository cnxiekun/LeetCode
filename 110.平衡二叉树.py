#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 228/228 cases passed (40 ms)
    # Your runtime beats 98.11 % of python3 submissions
    # Your memory usage beats 77.33 % of python3 submissions (18.7 MB)
    def isBalanced(self, root: TreeNode) -> bool:
        """深度优先搜索：DFS --> 递归"""
        return self.depth(root) != -1

    def depth(self, node):
        if not node:
            return 0
        l = self.depth(node.left)
        r = self.depth(node.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)
# @lc code=end

 