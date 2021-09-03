#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 62/62 cases passed (40 ms)
        # Your runtime beats 84.8 % of python3 submissions
        # Your memory usage beats 17.4 % of python3 submissions (15.8 MB)
        if not head or not head.next:
            return head
        a = b = head

        # 不足 k 个节点，不需要反转
        for i in range(k):
            if not b:
                return head
            b = b.next

        # 反转 k 个节点
        res = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return res

    
    def reverse(self, a, b):
        """
        反转 [a, b) 之间的节点
        """
        res = None
        while a != b:
            res, res.next, a = a, res, a.next
        return res

# @lc code=end

