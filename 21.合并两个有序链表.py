#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 208/208 cases passed (44 ms)
        # Your runtime beats 51.59 % of python3 submissions
        # Your memory usage beats 32.73 % of python3 submissions (15 MB)
        if not l1 or not l2:
            return l1 or l2
        head = ListNode()
        current = head
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return head.next
# @lc code=end

