#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 294/294 cases passed (36 ms)
        # Your runtime beats 80.77 % of python3 submissions
        # Your memory usage beats 7.52 % of python3 submissions (15.1 MB)
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == "1" and b[-1] == "1":
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), "1") + "0"
        elif a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[:-1], b[:-1]) + "0"
        else:
            return self.addBinary(a[:-1], b[:-1]) + "1"

        # 294/294 cases passed (32 ms)
        # Your runtime beats 91.74 % of python3 submissions
        # Your memory usage beats 14.11 % of python3 submissions (15 MB)
        # def addRemaning(aList, tmp):
        #     res = ""
        #     count, pop_count = 0, len(aList)
        #     while count < pop_count:
        #         a = aList.pop()
        #         num = int(a) + tmp
        #         res = str(num % 2) + res
        #         tmp = num // 2
        #         count += 1
        #     res = str(tmp) + res if tmp == 1 else res
        #     return res
        
        # aList, bList = list(a), list(b)
        # res = ""
        # count, pop_count = 0, min(len(aList), len(bList))
        # tmp = 0
        # while count < pop_count:
        #     a, b = aList.pop(), bList.pop()
        #     num = int(a) + int(b) + tmp
        #     res = str(num % 2) + res
        #     tmp = num // 2
        #     count += 1
        # if aList:
        #     res = addRemaning(aList, tmp) + res
        # else:
        #     res = addRemaning(bList, tmp) + res
        # return res
# @lc code=end

