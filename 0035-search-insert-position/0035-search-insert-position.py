class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, element in enumerate(nums):
            if element == target:
                return i
            elif element > target:
                return i
        return len(nums)