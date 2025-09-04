class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = 0
        for i in range(len(nums)):
            rightSum = sum(nums[i+1:])
            print(i, "leftSum: ", leftSum, "rightSum:", rightSum)

            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]
        
        return -1