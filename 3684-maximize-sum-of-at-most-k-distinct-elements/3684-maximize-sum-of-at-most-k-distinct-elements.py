class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(list(set(nums)), reverse=True)

        if len(nums)>=k:
            return nums[:k]
            
        return nums