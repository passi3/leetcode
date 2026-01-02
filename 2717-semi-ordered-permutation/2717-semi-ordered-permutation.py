class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        return nums.index(1) + len(nums) - 1 - nums.index(len(nums)) - int(nums.index(1) > nums.index(len(nums)))