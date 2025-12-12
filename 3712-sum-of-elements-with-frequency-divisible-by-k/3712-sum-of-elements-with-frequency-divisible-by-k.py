class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        res = 0
        for num in set(nums):
            freq = nums.count(num)
            if freq % k == 0:
                res += num * freq
        
        return res