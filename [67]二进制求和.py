# 给定两个二进制字符串，返回他们的和（用二进制表示）。 
# 
#  输入为非空字符串且只包含数字 1 和 0。 
# 
#  示例 1: 
# 
#  输入: a = "11", b = "1"
# 输出: "100" 
# 
#  示例 2: 
# 
#  输入: a = "1010", b = "1011"
# 输出: "10101" 
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addRestNum(self, c: str, tmp: int) -> str:
        res = ""
        for n in c:
            num = int(n) + tmp
            if num < 2:
                res += str(num)
                tmp = 0
            else:
                res += str(num - 2)
                tmp = 1
        if tmp == 1:
            res += "1"
        return res

    def addBinary(self, a: str, b: str) -> str:
        tmp = 0
        a = a[::-1]
        b = b[::-1]
        res = ""
        count = min(len(a), len(b))
        for i in range(count):
            num = int(a[i]) + int(b[i]) + tmp
            if num < 2:
                res += str(num)
                tmp = 0
            else:
                res += str(num - 2)
                tmp = 1
        if count < len(a):
            res += self.addRestNum(a[count:], tmp)
        elif count < len(b):
            res += self.addRestNum(b[count:], tmp)
        elif tmp == 1:
            res += "1"
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
