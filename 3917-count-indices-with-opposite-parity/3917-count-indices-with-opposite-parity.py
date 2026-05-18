class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        nums = list(map(lambda x: x % 2, nums))
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            res[i] = sum(1 for x in nums[i+1:] if x != num)

        return res