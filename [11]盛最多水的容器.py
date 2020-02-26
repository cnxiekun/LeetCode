# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, 
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  说明：你不能倾斜容器，且 n 的值至少为 2。
# 
#  
# 
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  
# 
#  示例:
# 
#  输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49 
#  Related Topics 数组 双指针

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 暴力解法复杂度O(N^2)：超时了
        # res = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         res = max(res, (j-i) * min(height[i], height[j]))
        # return res
        """
        使用双指针方法，一个从最左边开始，一个从最右边开始，计算两个挡板之间的面积，然后在向中间移动
        移动规则：如果哪个挡板比较矮，就舍弃掉这个挡板，把指向这个挡板的指针向中间移动
        """
        left = 0
        right = len(height) - 1
        res = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            res = max(res, (right - left) * min(height[left], height[right]))
        return res
# leetcode submit region end(Prohibit modification and deletion)
