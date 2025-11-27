class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        for i in range(length):
            if length % (i+1) == 0:
                res += nums[i]**2

        return res
        