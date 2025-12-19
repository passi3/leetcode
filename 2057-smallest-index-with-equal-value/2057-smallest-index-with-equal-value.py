class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        indices = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                indices.append(i)
        
        return min(indices) if len(indices) > 0 else -1