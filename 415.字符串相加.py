#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 317/317 cases passed (44 ms)
        # Your runtime beats 76.7 % of python3 submissions
        # Your memory usage beats 20.48 % of python3 submissions (15.2 MB)
        if len(num1) >= len(num2):
            num2 = "0" * (len(num1) - len(num2)) + num2
        else:
            num1 = "0" * (len(num2) - len(num1)) + num1
        res, carry = "", 0
        for i in range(len(num1)-1, -1, -1):
            num = int(num1[i]) + int(num2[i]) + carry
            res = str(num % 10) + res
            carry = num // 10
        
        return '1' + res if carry else res
# @lc code=end

