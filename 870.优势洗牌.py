#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        田忌赛马：最强打最强，打得过就上，打不过就用最差的对战
        """
        n = len(nums1)
        nums1 = sorted(nums1)
        
        # nums2降序排对应的index顺序
        order = sorted(range(n), key=lambda x: nums2[x], reverse=True)
        
        res = [None] * n
        left, right = 0, n-1
        for i in order:
            if nums1[right] > nums2[i]:
                res[i] = nums1[right]
                right -= 1
            else:
                res[i] = nums1[left]
                left +=1
        return res
# @lc code=end

