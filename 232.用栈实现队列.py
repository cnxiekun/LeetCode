#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    # 21/21 cases passed (24 ms)
    # Your runtime beats 98.62 % of python3 submissions
    # Your memory usage beats 73.38 % of python3 submissions (15 MB)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        n = len(self.stack1) - 1
        for i in range(n):
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        for i in range(n):
            self.stack1.append(self.stack2.pop())
        return res


    def peek(self) -> int:
        """
        Get the front element.
        """
        # n = len(self.stack1) - 1
        # for i in range(n):
        #     self.stack2.append(self.stack1.pop())
        # res = self.stack1[0]
        # for i in range(n):
        #     self.stack1.append(self.stack2.pop())
        # return res
        return self.stack1[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

