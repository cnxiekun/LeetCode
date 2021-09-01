#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 266/266 cases passed (104 ms)
        # Your runtime beats 43.08 % of python3 submissions
        # Your memory usage beats 92.85 % of python3 submissions (15 MB)
        if not t or not s:
            return ""
        # 不可以用 window = need = {}
        window, need = {}, {}
        valid = 0
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        left = right = 0
        start, end = 0, len(s) + 1
        # 滑动窗口：[start, right) 左闭右开
        while right < len(s):
            c = s[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            if c in need and window[c] == need[c]:
                valid += 1
            
            while valid == len(need):
                if right - left < end - start:
                    start, end = left, right
                
                c = s[left]
                left += 1
                if c in need and window[c] == need[c]:
                    valid -= 1
                window[c] -= 1
        
        if end == len(s) + 1:
            return ""
        else:
            return s[start:end]
# @lc code=end

