#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        """
        DP table 减少重复计算
        核心：每个节点都可以作为根节点
        """
        # 19/19 cases passed (32 ms)
        # Your runtime beats 69.75 % of python3 submissions
        # Your memory usage beats 34.27 % of python3 submissions (15 MB)
        self.dp = [[None] * (n+1) for _ in range(n+1)]
        return self.count(1, n)
    

    def count(self, low, high):
        """
        统计 [low, high] 区间内的组合数
        """
        if low > high:
            return 1
        
        # 优先查看是否已计算好，用缓存值
        if self.dp[low][high]:
            return self.dp[low][high]
        
        res = 0
        for i in range(low, high+1):
            # 区间内任意元素都可以作为根节点
            left, right = self.count(low, i-1), self.count(i+1, high)
            res += left * right
            self.dp[low][high] = res
        return res
# @lc code=end

