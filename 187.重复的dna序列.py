#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        left, right = 0, 0
        window, seen = [], {}
        while right < len(s):
            # 扩大窗口，加入s[right]
            window.append(s[right])
            right += 1

            # window达到要求是
            if right - left == 10:
                window_str = ''.join(window)
                if window_str in seen and window_str not in res:
                    res.append(window_str)
                else:
                    seen[window_str] = 1
                
                # 缩小窗口，移除s[left]
                window = window[1:]
                left += 1
        
        return res
# @lc code=end

