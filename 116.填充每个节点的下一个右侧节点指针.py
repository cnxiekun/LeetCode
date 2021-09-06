#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        二叉树前序遍历 —— 递归：深度优先搜索，定义连接两个节点的辅助函数
        """
        # 58/58 cases passed (164 ms)
        # Your runtime beats 12.1 % of python3 submissions
        # Your memory usage beats 6.13 % of python3 submissions (16.7 MB)
        if not root or not root.left:
            return root

        self.connectTwoNodes(root.left, root.right)
        return root
    
    def connectTwoNodes(self, node1, node2):
        if not node1:
            return node1
        
        # **** 前序遍历位置 ****
        # 将传入的两个节点连接
        node1.next = node2
        # 连接相同父节点的两个子节点
        self.connectTwoNodes(node1.left, node1.right)
        self.connectTwoNodes(node2.left, node2.right)
        # 连接跨越父节点的两个子节点
        self.connectTwoNodes(node1.right, node2.left)
# @lc code=end

