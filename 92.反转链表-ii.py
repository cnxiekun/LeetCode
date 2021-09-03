#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 44/44 cases passed (32 ms)
        # Your runtime beats 77.66 % of python3 submissions
        # Your memory usage beats 5.1 % of python3 submissions (15.5 MB)
        if left == 1:
            return self.reverseN(head, right)
        
        self.last = None
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

    def reverseN(self, head, n):
        if n == 1:
            self.last = head.next
            return head
        res = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.last
        return res
# @lc code=end

