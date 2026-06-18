class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = [num for num in nums if num % 2 ==0 and num % 3 == 0]
        return 0 if len(nums) == 0 else int(sum(nums)/len(nums))
