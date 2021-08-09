#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """迭代 -- 根、左、右"""
        # 69/69 cases passed (28 ms)
        # Your runtime beats 94.55 % of python3 submissions
        # Your memory usage beats 6.24 % of python3 submissions (15.1 MB)
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

        """递归"""
        # 69/69 cases passed (28 ms)
        # Your runtime beats 94.55 % of python3 submissions
        # Your memory usage beats 53.6 % of python3 submissions (14.9 MB)
        if not root:
            return []
        # if not root.left and not root.right:
        #     return [root.val]
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
# @lc code=end

