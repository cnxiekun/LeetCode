# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三
# 元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N < 3:
            return []
        nums.sort()
        res = []
        # 固定最左边的值
        for left in range(N - 2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = N - 1
            while mid < right:
                tmp_sum = nums[left] + nums[mid] + nums[right]
                if tmp_sum == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right+1]:
                        right -= 1
                elif tmp_sum < 0:
                    mid += 1
                else:
                    right -= 1
        # 以下感觉是种改进方法，但一直超时，不知为何：按理算法复杂度还会更低一些
        # for left in range(N - 2):
        #     if left > 0 and nums[left] == nums[left-1]:
        #         continue
        #     right = N - 1
        #     if nums[left] > 0 or nums[right] < 0:
        #         break
        #     while left < right - 1:
        #         tmp_sum = -(nums[left] + nums[right])
        #         if tmp_sum in nums[left+1:right]:
        #             res.append([nums[left], tmp_sum, nums[right]])
        #         right -= 1
        #         while left < right - 1 and nums[right] == nums[right+1]:
        #             right -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
