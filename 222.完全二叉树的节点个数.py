#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 18/18 cases passed (60 ms)
        # Your runtime beats 95.13 % of python3 submissions
        # Your memory usage beats 6.89 % of python3 submissions (21.9 MB)
        left, right = root, root
        h_left = h_right = 0
        while left:
            left = left.left
            h_left += 1
        
        while right:
            right = right.right
            h_right += 1

        # 判断是否是满二叉树: 左右子树的高度是否相同
        if h_left == h_right:
            return 2 ** h_left - 1
        
        # 否则按照正常二叉树统计节点数
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# @lc code=end

