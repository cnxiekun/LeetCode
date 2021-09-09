#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        DP
        """
        # 8/8 cases passed (68 ms)
        # Your runtime beats 9.32 % of python3 submissions
        # Your memory usage beats 66.11 % of python3 submissions (16.5 MB)
        return self.build(1, n)


    def build(self, low, high):
        """
        构建 [low, high] 区间内的所有BST
        """
        if low > high:
            return [None]
        
        res = []
        for i in range(low, high+1):
            # 区间内任意元素都可以作为根节点
            left, right = self.build(low, i-1), self.build(i+1, high)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left, root.right = l, r
                    res.append(root)
        return res
# @lc code=end

