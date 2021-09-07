#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 93/93 cases passed (52 ms)
        # Your runtime beats 61.03 % of python3 submissions
        # Your memory usage beats 86.33 % of python3 submissions (18.6 MB)
        self.count, self.value, self.k = 0, None, k
        
        self.traverse(root)
        return self.value
        

    def traverse(self, root):
        if not root:
            return
        
        # 中序遍历
        self.traverse(root.left)
        self.count += 1
        
        if self.count == self.k:
            self.value = root.val
            return
        self.traverse(root.right)
        # return self.value

# @lc code=end

