class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zeros = nums.count(0)
        return zeros - nums[(-1)*zeros:].count(0)