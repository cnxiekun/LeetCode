#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) < 3:
        #     return []
        # nums = sorted(nums)
        # res = []
        # for i in range(len(nums) - 2):
        #     seen = {}
        #     target = -nums[i]
        #     for j in range(i+1, len(nums)):
        #         remaning = target - nums[j]
        #         if remaning in seen:
        #             # tmp = sorted([nums[i], remaning, nums[j]])
        #             tmp = [nums[i], remaning, nums[j]]
        #             if tmp not in res:
        #                 res.append(tmp)
        #         else:
        #             seen[nums[j]] = j
        # return res
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # 跳过重复结果
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            two_sum_tmp = self.twoSum(nums[i+1:], target)
            if two_sum_tmp:
                res += [[nums[i]] + two_sum for two_sum in two_sum_tmp]
        return res

    def twoSum(self, nums, target):
        """
        nums: 已排序, 返回所有两数之和为target的所有不重复的结果
        """
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            l, r, s = nums[left], nums[right], nums[left] + nums[right]
            if s == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == l:
                    left += 1
                while left < right and nums[right] == r:
                    right -= 1
            elif s > target:
                while left < right and nums[right] == r:
                    right -= 1
            elif s < target:
                while left < right and nums[left] == l:
                    left += 1
        return res
# @lc code=end

