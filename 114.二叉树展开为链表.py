#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        后续遍历：递归 —— 深度优先搜索
        """
        # 225/225 cases passed (24 ms)
        # Your runtime beats 99.49 % of python3 submissions
        # Your memory usage beats 49.43 % of python3 submissions (15 MB)
        if not root:
            return root
        
        # 分别拉平左右节点
        self.flatten(root.left)
        self.flatten(root.right)

        # ***后续遍历***
        left, right = root.left, root.right
        # 右节点 接到 左节点上
        if left:
            node = left
            while node.right:
                node = node.right
            node.right = right
        else:
            left = right

        # 左节点 移到 右节点上
        root.left = None
        root.right = left

# @lc code=end

