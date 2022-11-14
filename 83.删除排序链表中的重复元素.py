#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 166/166 cases passed (44 ms)
        # Your runtime beats 65.47 % of python3 submissions
        # Your memory usage beats 34.51 % of python3 submissions (15 MB)
        # curr = head
        # while curr:
        #     while curr.next and curr.val == curr.next.val:
        #         curr.next = curr.next.next
        #     curr = curr.next
        # return head
        if not head:
            return head
        
        slow, fast = head, head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head
# @lc code=end

