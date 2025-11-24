class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eSum = 0
        dSum = 0
        for num in nums:
            eSum += num
            while num:
                num, d = divmod(num, 10)
                dSum += d
        return abs(eSum - dSum)