class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return sum(nums[:-k-1:-1]) - sum(nums[:k])