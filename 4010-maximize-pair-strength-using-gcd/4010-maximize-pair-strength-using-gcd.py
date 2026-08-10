class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        def gcd(num1: int, num2: int) -> int:
            while num2:
                num1, num2 = num2, num1 % num2
            return num1
        
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                res = max(res, nums[i]*nums[j] // (gcd(nums[i], nums[j])**2))
        
        return res