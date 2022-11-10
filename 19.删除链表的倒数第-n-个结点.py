#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建虚拟头结点，避免边界问题：head=[1] & n=1
        p = ListNode()
        p.next = head
        
        # 先找到倒数第n+1个节点，利用双指针，p1先走n+1步，然后p2=head，p1 & p2同时走，直到p1遍历完
        p1 = p
        for _ in range(n+1):
            p1 = p1.next
        p2 = p
        while p1:
            p1, p2 = p1.next, p2.next
        
        # 此时p2的首个节点就是head的倒数第n+1个节点
        p2.next = p2.next.next
        return p.next
# @lc code=end

