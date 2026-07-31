class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        priority = set(nums[:k])

        if len(priority) < len(nums[:k]):
            return True
        
        if len(nums) < k:
            return False

        for i in range(k, len(nums)):
            if nums[i] in priority:
                return True
            
            priority.add(nums[i])
            priority.remove(nums[i-k])
        
        return False