#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) <= 1:
        #     return len(s)
        # res = 1
        # curr = prev = s[0]
        # for char in s[1:]:
        #     if char in prev:
        #         curr = prev[prev.index(char) + 1:] + char
        #     else:
        #         curr = prev + char
        #     res = max(res, len(curr))
        #     prev = curr
        # return res
        """
        滑动窗口解法
        """
        if len(s) <= 1:
            return len(s)
        
        res = 1
        left, right = 0, 0
        window = {}
        # 增大窗口
        while right < len(s):
            c = s[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
        
            # 判断是否需要收缩窗口
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left)
        
        return res
# @lc code=end

