class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = list()
        for num in nums:
            for char in str(num):
                res.append(int(char))
        return res