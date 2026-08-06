class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        res = []
        total = sum(nums)
        nums.sort(reverse=True)
        
        i = 0
        while sum(res) <= total/2:
            res.append(nums[i])
            i+= 1
        
        return res