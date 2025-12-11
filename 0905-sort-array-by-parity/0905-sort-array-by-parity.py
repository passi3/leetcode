class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [num for num in nums if num % 2 == 0]
        res += [num for num in nums if num % 2 == 1]
        return res