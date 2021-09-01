#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 106/106 cases passed (80 ms)
        # Your runtime beats 46.84 % of python3 submissions
        # Your memory usage beats 54.01 % of python3 submissions (15 MB)
        if len(s1) > len(s2):
            return False
        if not s1:
            return True
        # 不可以用 window = need = {}
        window, need = {}, {}
        valid = 0
        for c in s1:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        left = right = 0

        # 滑动窗口：[start, right) 左闭右开
        while right < len(s1):
            c = s2[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            if c in need and window[c] == need[c]:
                valid += 1
        
        if valid == len(need):
            return True

        # 否则开始向右滑动一个位置
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            if c in need and window[c] == need[c]:
                valid += 1
                
            c = s2[left]
            left += 1
            if c in need and window[c] == need[c]:
                valid -= 1
            window[c] -= 1

            if valid == len(need):
                return True
        
        return False 
# @lc code=end

