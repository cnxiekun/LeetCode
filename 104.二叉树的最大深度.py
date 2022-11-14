#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        递归
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    #     """
    #     迭代
    #     """
    #     self.res, self.depth = 0, 0
    #     self.traverse(root)
    #     return self.res

    # def traverse(self, root):
    #     if not root:
    #         return
        
    #     self.depth += 1
    #     if not root.left and not root.right:
    #         self.res = max(self.res, self.depth)
        
    #     self.traverse(root.left)
    #     self.traverse(root.right)
    #     self.depth -= 1
# @lc code=end

