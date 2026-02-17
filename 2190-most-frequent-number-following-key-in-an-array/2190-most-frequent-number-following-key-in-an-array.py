class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        h = dict()
        for i, num in enumerate(nums[:-1]):
            if num == key:
                h[nums[i+1]] = h.get(nums[i+1], 0) + 1
        
        target = max(h.values())
        
        for k, val in h.items():
            if val == target:
                return k