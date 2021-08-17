#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 34/34 cases passed (48 ms)
        # Your runtime beats 56.78 % of python3 submissions
        # Your memory usage beats 55.61 % of python3 submissions (15.3 MB)
        if len(intervals) <= 1:
            return len(intervals)
        
        # 起点升序，终点降序排！！
        intervals.sort(key=lambda x:(x[0], -x[1]))
        start, end = intervals[0][0], intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            if interval[0] >= start and interval[1] <= end:
                res += 1
            elif interval[0] < end:
                end = interval[1]
            else:
                start, end = interval[0], interval[1]
        return len(intervals) - res
# @lc code=end

