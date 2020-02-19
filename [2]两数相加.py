# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        res = head
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l1, l2 = l1.next, l2.next
        l = l1 if l1 else l2
        while l:
            add = l.val + carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l = l.next
        if carry:
            head.next = ListNode(1)
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
