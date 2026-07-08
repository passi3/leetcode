class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)

        prefix = [0] * l
        suffix = [0] * l

        prefix[0] = nums[0]
        for i in range(1, l):
            prefix[i] = max(prefix[i-1], nums[i])
        
        suffix[-1] = nums[-1]
        for i in range(l-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i])

        for i in range(l):
            if abs(prefix[i] - suffix[i]) <= k:
                return i
        
        return -1