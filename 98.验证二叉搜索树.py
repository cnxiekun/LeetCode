#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 80/80 cases passed (52 ms)
        # Your runtime beats 35.34 % of python3 submissions
        # Your memory usage beats 72.04 % of python3 submissions (17.2 MB)
        return self.isValidBSTHelper(root, None, None)
    

    def isValidBSTHelper(self, root, min_node, max_node):
        """
        限定以 root 为根的子树节点必须满足 
        max_node.val > root.val > min_node.val */
        """
        if not root:
            return True
        if min_node and root.val <= min_node.val:
            return False
        if max_node and root.val >= max_node.val:
            return False
        
        # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
        return self.isValidBSTHelper(root.left, min_node, root) and self.isValidBSTHelper(root.right, root, max_node)
# @lc code=end

