#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        # 初始化need字段，每个字符分别需要出现几次
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        valid = 0
        left, right = 0, 0
        start, end = 0, len(s) + 1
        while right < len(s):
            # 增大滑动窗口：添加元素c
            c = s[right]
            right += 1
            # 更新窗口内数据
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1
            
            # 判断是否需要收缩窗口
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < end - start:
                    start, end  = left, right
                # 缩小滑动窗口：移除元素c
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return s[start:end] if end != len(s) + 1 else ""
# @lc code=end

