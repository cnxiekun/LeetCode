#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
from collections import OrderedDict
class LRUCache:
    # 21/21 cases passed (480 ms)
    # Your runtime beats 63.04 % of python3 submissions
    # Your memory usage beats 12.12 % of python3 submissions (70.1 MB)

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.lrucache = OrderedDict()


    def get(self, key: int) -> int:
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        return self.lrucache.get(key, -1)


    def put(self, key: int, value: int) -> None:
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        elif len(self.lrucache) == self.max_capacity:
            self.lrucache.popitem(last=False)
        self.lrucache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

