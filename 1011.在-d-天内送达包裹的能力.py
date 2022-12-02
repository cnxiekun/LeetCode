#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        二分法查找
        辅助函数：给定运载能力capacity，返回多少天能运完
        然后二分法找左边界
        """
        # 运载能力边界
        left_capacity, right_capacity = max(weights), sum(weights)
        while left_capacity <= right_capacity:
            med_capacity = (left_capacity + right_capacity) // 2
            need_days = self.shipWithinCapacity(weights, med_capacity)
            if need_days <= days:
                right_capacity = med_capacity - 1
            else:
                left_capacity = med_capacity + 1
        return left_capacity


    def shipWithinCapacity(self, weights, capacity):
        if not weights:
            return 0
        days, curr = 1, 0
        for w in weights:
            if curr + w <= capacity:
                curr += w
            else:
                curr = w
                days += 1
        return days
# @lc code=end

