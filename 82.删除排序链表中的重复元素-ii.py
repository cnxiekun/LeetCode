#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # """递归"""
        # # 166/166 cases passed (52 ms)
        # # Your runtime beats 96.73 % of python3 submissions
        # # Your memory usage beats 59.2 % of python3 submissions (15 MB)
        # if not head or not head.next:
        #     return head
        # if head.val != head.next.val:
        #     head.next = self.deleteDuplicates(head.next)
        # else:
        #     move = head.next
        #     while move and move.val == head.val:
        #         move = move.next
        #     return self.deleteDuplicates(move)
        # return head
        
        """迭代"""
        # 166/166 cases passed (36 ms)
        # Your runtime beats 89.08 % of python3 submissions
        # Your memory usage beats 9.18 % of python3 submissions (15.1 MB)
        if not head or not head.next:
            return head
        res = current = ListNode(0)
        res.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                current.next = head
            else:
                current = current.next
                head = head.next
        return res.next
# @lc code=end

