class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        if 1 not in nums or 2 not in nums:
            return -1
        
        res = float("inf")
        prev = None
        idx = -1

        for i, num in enumerate(nums):
            if num not in [1, 2]:
                continue

            if prev is None:
                prev = num
                idx = i
            elif num != prev:
                res = min(res, i - idx)
                prev = num
                idx = i
            else:
                idx = i
        
        return res