class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        for num in set(nums):
            if nums.count(num) == 1:
                res += num
        
        return res