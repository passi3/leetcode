class Solution:
    def addDigits(self, num: int) -> int:
        while num//10 > 0:
            q, r = num // 10, num % 10
            num = q+r
        return num