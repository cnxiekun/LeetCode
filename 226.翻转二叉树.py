#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """递归: 深度优先遍历"""
        # 77/77 cases passed (24 ms)
        # Your runtime beats 98.74 % of python3 submissions
        # Your memory usage beats 27.92 % of python3 submissions (15 MB)
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        # """迭代：广度优先遍历"""
        # # 77/77 cases passed (40 ms)
        # # Your runtime beats 44.12 % of python3 submissions
        # # Your memory usage beats 14.45 % of python3 submissions (15 MB)
        # if not root:
        #     return root
        # queue = [root]
        # while queue:
        #     tmp = queue.pop()
        #     tmp.left, tmp.right = tmp.right, tmp.left
        #     if tmp.left:
        #         queue.append(tmp.left)
        #     if tmp.right:
        #         queue.append(tmp.right)
        # return root
# @lc code=end

