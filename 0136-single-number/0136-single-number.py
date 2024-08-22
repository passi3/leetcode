class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for element in nums:
            output ^= element
        return output