#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.dp(root)
        return max(res[0], res[1])
    
    def dp(self, root):
        """
        返回二维数组 [res[0], [res[1]]]
        res[0]: 不抢root带来的最大收益
        res[1]: 抢root带来的最大收益
        """
        if not root:
            return [0, 0]
        
        left = self.dp(root.left)
        right = self.dp(root.right)

        not_rob = max(left[0], left[1]) + max(right[0], right[1])
        rob = root.val + left[0] + right[0]
        return [not_rob, rob]
# @lc code=end

