class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            x = min(nums)
            i = nums.index(x)
            nums[i] = x * multiplier
        return nums