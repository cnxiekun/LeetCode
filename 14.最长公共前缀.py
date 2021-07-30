#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 123/123 cases passed (32 ms)
        # Your runtime beats 91.81 % of python3 submissions
        # Your memory usage beats 10.93 % of python3 submissions (15.1 MB)
        lengths = [len(s) for s in strs]
        min_len = min(lengths)
        min_str = strs[lengths.index(min_len)]
        for i in range(min_len, 0, -1):
            if min([s[:i] == min_str[:i] for s in strs]):
                return min_str[:i]
        return ""

# @lc code=end

