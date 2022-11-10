#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res_1, res_2 = ListNode(), ListNode()
        curr_1, curr_2 = res_1, res_2
        while head:
            if head.val < x:
                curr_1.next = head
                curr_1 = curr_1.next
            else:
                curr_2.next = head
                curr_2 = curr_2.next
    
            head = head.next
        
        curr_2.next = None
        curr_1.next = res_2.next
        return res_1.next
# @lc code=end

