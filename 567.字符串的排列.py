#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2 or len(s1) > len(s2):
            return False
        
        need, window = {}, {}
        valid, left, right = 0, 0, 0
        for c in s1:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        
        # 滑动窗口：始终保持窗口长度与s1等长
        # [left, right)
        # 初始化window，保持与s1一样大小
        while right < len(s1):
            # window中新增需要加入的字符
            c = s2[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
            # 判断当前字符c是否满足要求
            if c in s1 and need[c] == window[c]:
                valid += 1
        
        # 此时初始化window已完成，即选取了s2中前len(s1)个元素
        # 首次判断是否符合
        if valid == len(need):
            return True
        
        # 否则移动窗口：窗口+1、窗口-1
        while right < len(s2):
            # 窗口right+1
            c = s2[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
            
            if c in s1 and need[c] == window[c]:
                valid += 1
            
            # 窗口left+1
            c = s2[left]
            left += 1

            if c in s1 and need[c] == window[c]:
                valid -= 1
            window[c] -= 1
            
            if valid == len(need):
                return True
            
        return False
# @lc code=end

