class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            digits = []
            while num > 0:
                digits.append(num%10)
                num //= 10
            for i in range(len(digits)):
                res += max(digits)*10**i
        return res