class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum(nums[:2]) - nums[-1]