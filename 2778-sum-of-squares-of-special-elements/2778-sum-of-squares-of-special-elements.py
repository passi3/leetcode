class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length = len(nums)
        res = []
        for i in range(length):
            if length % (i+1) == 0:
                res.append(nums[i]**2)

        return sum(res)
        