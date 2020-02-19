# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划

# 与第3题无重复自负的最长子串类似
# DP解法：f(i)表示代表***以当前第n个数据位置为结尾***的最大子串的和，比较f(1), ..., f(n)的最大值即可

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        current_max = nums[0]
        prev_max = nums[0]
        res = nums[0]
        for num in nums[1:]:
            current_max = num + prev_max if prev_max > 0 else num
            prev_max = current_max
            res = max(res, current_max)
        return res
# leetcode submit region end(Prohibit modification and deletion)
