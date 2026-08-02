class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        indices = [1]*l
        
        for i in range(1,l):
            if nums[i] > nums[i-1]:
                indices[i] = indices[i-1] + 1
        
        for i in range(l-2*k+1):
            if indices[i+k-1]>= k and indices[i+2*k-1]>=k:
                return True
                
        return False     