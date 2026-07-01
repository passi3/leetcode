class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l

        for i, num in enumerate(nums):
            nxt = (i + num) % l
            res[i] = nums[nxt]
        
        return res