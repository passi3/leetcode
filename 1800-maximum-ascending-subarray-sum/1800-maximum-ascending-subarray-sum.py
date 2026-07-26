class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev = -1
        res = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] > prev:
                temp += nums[i]
            else:
                temp = nums[i]
            prev = nums[i]
            res = max(res, temp)
        
        return res
            