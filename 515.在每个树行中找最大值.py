#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # """
        # 深度优先搜索：前序遍历
        # """
        # res = []
        # def dfs(root, depth):
        #     if not root:
        #         return
        #     # 初始化res[depth]的值
        #     if depth == len(res):
        #         res.append(root.val)
        #     else:
        #         # 更新res[depth]的值
        #         res[depth] = max(res[depth], root.val)
        #     # 前序遍历递归
        #     dfs(root.left, depth + 1)
        #     dfs(root.right, depth + 1)
        
        # dfs(root, 0)
        # return res
        """
        广度优先搜索：队列保存当前层的所有节点
        """
        if not root:
            return []
        res = []
        # 初始化第一层节点
        queue = [root]
        while queue:
            max_tmp = float("-inf")
            q_tmp = queue
            queue = []
            # 遍历当前层的所有节点，并更新当前层的最大值
            for node in q_tmp:
                max_tmp = max(max_tmp, node.val)
                # 初始化下一层的所有节点至queue中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_tmp)
        return res
# @lc code=end

