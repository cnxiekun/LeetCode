# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。 
# 
#  示例： 
# 
#  给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#  
# 
#  说明： 
# 
#  给定的 n 保证是有效的。 
# 
#  进阶： 
# 
#  你能尝试使用一趟扫描实现吗？ 
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        # less than n nodes
        if not fast and count < n:
            return head
        # exactly n nodes
        if not fast and count == n:
            return head.next
        # more than n nodes
        slow = head
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
