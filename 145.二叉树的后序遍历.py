#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """迭代 -- 先根、右、左，再反过来"""
        # 68/68 cases passed (28 ms)
        # Your runtime beats 95 % of python3 submissions
        # Your memory usage beats 9.99 % of python3 submissions (15 MB)
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]

        # 68/68 cases passed (28 ms)
        # Your runtime beats 95 % of python3 submissions
        # Your memory usage beats 20.37 % of python3 submissions (15 MB)
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
# @lc code=end

