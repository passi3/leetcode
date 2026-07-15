class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = None
        
        for i, num in enumerate(nums):
            if nums[i] == 1:
                if prev is not None and i - prev - 1 < k:
                    return False
                else:
                    prev = i
        
        return True