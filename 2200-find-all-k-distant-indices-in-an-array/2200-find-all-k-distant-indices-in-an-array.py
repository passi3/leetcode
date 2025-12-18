class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        hash = {}
        keys = [i for i in range(len(nums)) if nums[i] == key]

        for i, num in enumerate(nums):
            dist = min([abs(key - i) for key in keys])
            hash[i] = dist
        
        return [i for i, v in hash.items() if v <= k]
            