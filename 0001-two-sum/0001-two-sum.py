class Solution(object):
    def twoSum(self, nums, target):
        if 2 <= len(nums) <= 10**4:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]