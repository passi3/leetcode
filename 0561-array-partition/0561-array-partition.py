class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)//2
        res = 0
        for i in range(l):
            res += nums[2*i]
        return res