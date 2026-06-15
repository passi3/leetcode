class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0

        while len(nums) != len(set(nums)):
            res += 1
            if len(nums) < 3:
                break
            nums = nums[3:]

        return res