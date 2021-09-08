#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 91/91 cases passed (68 ms)
        # Your runtime beats 34.47 % of python3 submissions
        # Your memory usage beats 87.53 % of python3 submissions (18.8 MB)
        if not root:
            return root
        if root.val == key:
            # 左、右分支存在空值情况，返回另一分支
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # 为了维持BST特点，可用左子树最大值、或者右子树最小值来“替换”要删除的节点
            # 以找出右子树最小值为例
            min_right_node = self.getMinRightNode(root.right)
            root.val = min_right_node.val
            root.right = self.deleteNode(root.right, min_right_node.val)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    
    def getMinRightNode(self, node):
        while node.left:
            node = node.left
        return node
# @lc code=end

