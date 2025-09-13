class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        cntEven, cntOdd = 0, 0
        for num in nums:
            if num % 2 == 0:
                cntEven += 1
            else:
                cntOdd += 1
        return ([0] * cntEven) + ([1] * cntOdd)