#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 91/91 cases passed (32 ms)
        # Your runtime beats 89.5 % of python3 submissions
        # Your memory usage beats 17.93 % of python3 submissions (15 MB)
        d = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in d.values():
                stack.append(char)
            else:
                if char in d.keys():
                    if not stack:
                        return False
                    if stack.pop() == d[char]:
                        pass
                    else:
                        return False
        if not stack:
            return True
        return False

# @lc code=end

