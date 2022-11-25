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
        
        # 滑动窗口：right先扩大，然后移动left，始终保持窗口长度与s1等长
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if need[c] == window[c]:
                    valid += 1
            
            # 判断是否需要收缩窗口, [left, right]
            while right - left >= len(s1):
                # 判断是否符合要求
                if valid == len(need):
                    return True
                c = s2[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return False
# @lc code=end

