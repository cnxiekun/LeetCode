#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 85/85 cases passed (624 ms)
        # Your runtime beats 76.6 % of python3 submissions
        # Your memory usage beats 88.31 % of python3 submissions (39.8 MB)
        """
        结合快慢指针——找出中间节点，优化空间
        """
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # 判断节点奇偶数
        if fast:
            slow = slow.next
        
        # 反转slow
        slow = self.reverse(slow)

        # 对比 slow 与 head
        while slow:
            if slow.val != head.val:
                return False
            slow, head = slow.next, head.next
        return True
    
    def reverse(self, slow):
        res, curr = None, slow
        while curr:
            res, res.next, curr = curr, res, curr.next
        return res
        
    #     """
    #     利用递归(链表后续遍历)模拟前后双指针判断
    #     """
    #     # 85/85 cases passed (856 ms)
    #     # Your runtime beats 15.99 % of python3 submissions
    #     # Your memory usage beats 6.61 % of python3 submissions (115.7 MB)
    #     self.left = head
    #     return self.traverse(head)
    
    # def traverse(self, right) -> bool:
    #     if not right:
    #         return True
    #     res = self.traverse(right.next)
    #     res = res and (self.left.val == right.val)
    #     self.left = self.left.next
    #     return res
# @lc code=end

