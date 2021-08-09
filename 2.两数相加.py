#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1568/1568 cases passed (60 ms)
        # Your runtime beats 77.13 % of python3 submissions
        # Your memory usage beats 52.8 % of python3 submissions (14.9 MB)
        head = ListNode()
        current = head
        carry = 0
        while l1 and l2:
            num = l1.val + l2.val + carry
            carry = num // 10
            current.next = ListNode(num % 10)
            current, l1, l2 = current.next, l1.next, l2.next
        remaining = l1 if l1 else l2
        while remaining:
            num = remaining.val + carry
            carry = num // 10
            current.next = ListNode(num % 10)
            current, remaining = current.next, remaining.next
        if carry == 1:
            current.next = ListNode(carry)
        return head.next
# @lc code=end

