# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 简单粗暴数组法
        # if not head:
        #     return head
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # res = res[::-1]
        # reversed_head = ListNode(None)
        # head = reversed_head
        # for _, val in enumerate(res):
        #     head.next = ListNode(val)
        #     head = head.next
        # return reversed_head.next

        # 经典链表哨兵法！！
        reversed_head = None
        current = head
        while current:
            reversed_head, reversed_head.next, current = current, reversed_head, current.next
        return reversed_head
# leetcode submit region end(Prohibit modification and deletion)
