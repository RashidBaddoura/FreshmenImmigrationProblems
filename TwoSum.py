class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if not nums[i] >= target:
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]