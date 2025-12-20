class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        length = len(nums)
        
        for i in range(length):
            if i-k >= 0:
                l = nums[i-k]
                if nums[i] <= l:
                    continue
            if i+k < length:
                r = nums[i+k]
                if nums[i] <= r:
                    continue
            res += nums[i]

        return res