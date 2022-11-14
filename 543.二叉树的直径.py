#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        递归：每一条二叉树的「直径」长度，就是一个节点的左右子树的最大深度之和
        """
        self.res = 0
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root):
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
# @lc code=end

