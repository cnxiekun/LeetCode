#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # """
        # 迭代
        # """
        # res = None
        # while head:
        #     res, res.next, head = head, res, head.next
        # return res

        """
        递归
        """
        if not head or not head.next:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
# @lc code=end

