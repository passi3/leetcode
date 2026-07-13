class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [-1] * l
        
        for i in range(l):
            if nums[i] == 2: 
                continue
            
            d = 1
            while nums[i] & d == d:
                res[i] = nums[i] - d
                d <<= 1
        
        return res