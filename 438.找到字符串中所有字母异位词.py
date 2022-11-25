#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []
    
        window, need = {}, {}
        valid, left, right = 0, 0, 0
        for c in p:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        left = right = 0

        # 滑动窗口：[start, right] 
        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            if c in need and window[c] == need[c]:
                valid += 1

            # 判断是否需要收缩窗口
            while right - left >= len(p):
                # 先判断是否符合要求
                if valid == len(need):
                    res.append(left)

                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        
        return res
# @lc code=end

