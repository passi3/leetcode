class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                newNum = nums[i] + 1
                cnt += newNum - nums[i+1]
                nums[i+1] = newNum
                
        return cnt