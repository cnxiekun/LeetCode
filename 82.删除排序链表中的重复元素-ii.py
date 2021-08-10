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
        # # Your runtime beats 26.85 % of python3 submissions
        # # Your memory usage beats 56.18 % of python3 submissions (15 MB)
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
        if not head or not head.next:
            return head
        res = current = ListNode(0)
        res.next = head
        while head and head.next:
            if head.val == head.next.val:
                move = head.next
                while move and move.next:
                    if move.val == move.next.val:
                        move = move.next
                head = move.next
                current.next = head
            else:
                current = current.next
                head = head.next
        return res.next
# @lc code=end

