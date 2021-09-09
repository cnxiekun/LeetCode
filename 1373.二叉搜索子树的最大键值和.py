#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        """
        二叉树 后序遍历
        """
        # 58/58 cases passed (392 ms)
        # Your runtime beats 64.21 % of python3 submissions
        # Your memory usage beats 74.54 % of python3 submissions (62.8 MB)
        self.max_sum = 0
        self.traverse(root)
        return self.max_sum

    
    def traverse(self, root):
        """
        return: [is_bst, min_val, max_val, bst_sum]
        是否是bst、节点最小值、节点最大值、节点和
        """
        if not root:
            return [1, float("inf"), -float("inf"), 0]
        left, right = self.traverse(root.left), self.traverse(root.right)

        if left[0] and right[0] and root.val > left[2] and root.val < right[1]:
            # 判断以root为根节点的树是否是BST
            res = [1, min(left[1], root.val), max(right[2], root.val), root.val + left[3] + right[3]]
            self.max_sum = max(self.max_sum, res[3])
        else:
            res = [0]
        return res
# @lc code=end

