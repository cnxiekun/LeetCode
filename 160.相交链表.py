#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        消除长度差... 两个指针分别遍历A/B、B/A
        """
        # 39/39 cases passed (148 ms)
        # Your runtime beats 84.49 % of python3 submissions
        # Your memory usage beats 55.34 % of python3 submissions (29.6 MB)
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1
# @lc code=end

