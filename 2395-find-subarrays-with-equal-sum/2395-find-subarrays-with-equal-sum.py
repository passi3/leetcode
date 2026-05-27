class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        
        for i in range(len(nums) - 1):
            target = nums[i] + nums[i+1]

            if target in seen:
                return True
            seen.add(target)
        
        return False