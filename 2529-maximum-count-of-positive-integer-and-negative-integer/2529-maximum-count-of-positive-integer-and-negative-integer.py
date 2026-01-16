class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        res = [0]*2
        for num in nums:
            if num > 0:
                res[0] += 1
            elif num < 0:
                res[1] += 1
        return max(res)