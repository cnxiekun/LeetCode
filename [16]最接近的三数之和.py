# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
# 
#  例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        res = sum(nums[:3])
        gap = abs(res - target)
        # 固定最左边的值
        for left in range(N - 2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = N - 1
            while mid < right:
                tmp_sum = nums[left] + nums[mid] + nums[right]
                if tmp_sum == target:
                    return tmp_sum

                if gap > abs(tmp_sum - target):
                    gap = abs(tmp_sum - target)
                    res = tmp_sum

                if tmp_sum < target:
                    mid += 1
                else:
                    right -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
