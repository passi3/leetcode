class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = nums[0]
        res = nums[0]

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp +=nums[i+1]
            else:
                temp = nums[i+1]
            
            res = max(temp, res)

        return res