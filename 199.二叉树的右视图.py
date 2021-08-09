#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 215/215 cases passed (32 ms)
        # Your runtime beats 87.71 % of python3 submissions
        # Your memory usage beats 44.85 % of python3 submissions (14.9 MB)
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            # 只存储当前层最后一个节点值
            res.append(queue[-1].val)
            # 下一层（所有节点）待处理
            tmp_queue = []
            for node in queue:
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            queue = tmp_queue
        return res
# @lc code=end

