class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr = nums[0]
        res = -1

        for num in nums[1:]:
            if num > curr:
                res = max(res, num - curr)
            else:
                curr = num
        
        return res