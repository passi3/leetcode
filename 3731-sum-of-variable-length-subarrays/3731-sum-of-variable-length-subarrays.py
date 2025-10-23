class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        arr = []

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            if 0 <= i < len(nums):
                arr += nums[max(0, i - nums[i]) : i + 1]
                
        return sum(arr)