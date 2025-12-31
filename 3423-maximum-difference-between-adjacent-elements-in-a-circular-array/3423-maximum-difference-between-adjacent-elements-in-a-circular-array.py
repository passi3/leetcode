class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            diff = abs(nums[i] - nums[(i+1)%len(nums)])
            if diff > res:
                res = diff

        return res