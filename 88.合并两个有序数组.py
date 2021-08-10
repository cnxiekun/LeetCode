#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        双指针从后往前，最大值放“当前”最后一位
        """
        # 59/59 cases passed (28 ms)
        # Your runtime beats 94.03 % of python3 submissions
        # Your memory usage beats 23 % of python3 submissions (15 MB)
        p1, p2, p3 = m-1, n-1, m+n-1
        while p1 >=0 or p2 >= 0:
            if p1 == -1:
                nums1[p2] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                p1 -= 1
            elif nums2[p2] >= nums1[p1]:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -=1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
                p3 -= 1
# @lc code=end

