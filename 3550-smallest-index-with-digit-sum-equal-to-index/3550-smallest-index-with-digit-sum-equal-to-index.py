class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            digitSum = 0
            while num > 0:
                q = num//10
                digitSum += num%10
                num //= 10
            
            if i == digitSum:
                return i
        
        return -1