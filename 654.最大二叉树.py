#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 107/107 cases passed (120 ms)
        # Your runtime beats 53.59 % of python3 submissions
        # Your memory usage beats 32.63 % of python3 submissions (15.5 MB)
        """
        递归：前序遍历
        """
        if not nums:
            return None
        
        # 找最大值
        max_i, max_v = 0, -float("inf")
        for i, v in enumerate(nums):
            if v > max_v:
                max_i, max_v = i, v
        
        root = TreeNode(max_v)
        root.left = self.constructMaximumBinaryTree(nums[:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        
        return root
# @lc code=end

