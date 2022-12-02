#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        二分法
        1、给定速度，返回吃完所有香蕉所需要的时间
        2、确定速度左右边界
        """
        left_speed, right_speed = 1, max(piles)
        while left_speed <= right_speed:
            med_speed = (left_speed + right_speed) // 2
            need_hours = self.minEatingHour(piles, med_speed)
            if need_hours <= h:
                # 可以减速
                right_speed = med_speed - 1
            else:
                # 需要加速
                left_speed = med_speed + 1
        return left_speed

    
    def minEatingHour(self, piles, speed):
        hours = 0
        for p in piles:
            hours += p // speed
            if p % speed > 0:
                hours += 1
        return hours
# @lc code=end

