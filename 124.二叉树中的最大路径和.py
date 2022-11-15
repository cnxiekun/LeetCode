#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # self.max_sum = float('-inf')

        # def traverse(root):
        #     if not root:
        #         return float('-inf')
            
        #     left = traverse(root.left)
        #     right = traverse(root.right)
        #     # 以下三种情况不可向上累加，因此设置全局变量存储不可累加的最大值
        #     # 向上累加：是指最大路劲和可包含当前根节点
        #     self.max_sum = max(self.max_sum, left, right, root.val + left + right)

        #     # 用递归返回可向上累加的最大值
        #     return max(root.val, root.val + left, root.val + right)
        
        # new_max = traverse(root)

        # return max(self.max_sum, new_max)
        self.max_sum = float('-inf')
        self.oneSideMax(root)
        return self.max_sum
    
    def oneSideMax(self, root):
        if not root:
            return 0
        
        left = max(0, self.oneSideMax(root.left))
        right = max(0, self.oneSideMax(root.right))
        self.max_sum = max(self.max_sum, root.val + left + right)

        return max(left, right) + root.val

# @lc code=end

