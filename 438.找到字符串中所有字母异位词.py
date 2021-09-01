#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 61/61 cases passed (80 ms)
        # Your runtime beats 79.81 % of python3 submissions
        # Your memory usage beats 14.11 % of python3 submissions (15.5 MB)
        if len(p) > len(s):
            return []

        res = []
    
        # 不可以用 window = need = {}
        window, need = {}, {}
        valid = 0
        for c in p:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        left = right = 0

        # 滑动窗口：[start, right) 左闭右开
        while right < len(p):
            c = s[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            if c in need and window[c] == need[c]:
                valid += 1
        
        if valid == len(need):
            res.append(0)

        # 否则开始向右滑动一个位置
        while right < len(s):
            c = s[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            if c in need and window[c] == need[c]:
                valid += 1
                
            c = s[left]
            left += 1
            if c in need and window[c] == need[c]:
                valid -= 1
            window[c] -= 1

            if valid == len(need):
                res.append(left)
        
        return res
# @lc code=end

