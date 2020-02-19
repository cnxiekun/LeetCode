# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window

# 与第53题最大自序和类似
# DP解法：f(i)表示代表***以当前第n个数据位置为结尾***的最长子串，比较len(f(1)), ..., len(f(n))的最大值即可

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        curr_max_sub, prev_max_sub = s[0], s[0]
        res = 1
        for st in s[1:]:
            # if st not in prev_max_sub, string find() function return -1
            curr_max_sub = curr_max_sub[prev_max_sub.find(st) + 1:] + st
            prev_max_sub = curr_max_sub
            res = max(len(curr_max_sub), res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
