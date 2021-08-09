#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 34/34 cases passed (24 ms)
        # Your runtime beats 98.87 % of python3 submissions
        # Your memory usage beats 38.76 % of python3 submissions (15.3 MB)
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            # 存储当前层
            res.append([node.val for node in queue])
            # 下一层(所有左右节点) 待处理
            tmp_queue = []
            for node in queue:
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            queue = tmp_queue
        return res[::-1]
# @lc code=end

