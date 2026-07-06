class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        target = len(nums) // 2
        return nums.count(nums[target]) == 1