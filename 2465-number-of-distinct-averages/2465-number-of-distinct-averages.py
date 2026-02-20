class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = set()
        nums.sort()
        while len(nums) > 0:
            res.add((nums[0] + nums[-1]) / 2)
            nums = nums[1:-1]
        return len(res)