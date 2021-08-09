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
        """迭代"""
        # 28/28 cases passed (48 ms)
        # Your runtime beats 28.42 % of python3 submissions
        # Your memory usage beats 29.11 % of python3 submissions (15.6 MB)
        # res = None
        # current = head
        # while current:
        #     res, res.next, current = current, res, current.next
        # return res

        """递归"""
        # 28/28 cases passed (32 ms)
        # Your runtime beats 93.29 % of python3 submissions
        # Your memory usage beats 15.39 % of python3 submissions (19.6 MB)
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
# @lc code=end

