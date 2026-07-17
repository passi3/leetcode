class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        res = 1
        target = sum(nums[:2])
        
        i = 2
        while i+1 < len(nums):
            if nums[i] + nums[i+1] != target:
                break
            res += 1
            i += 2
        
        return res