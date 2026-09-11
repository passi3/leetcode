class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        msb = -1 if x != abs(x) else 1

        digits = []
        x = abs(x)
        while x > 0:
            digits.append(x % 10)
            x //= 10

        for i, v in enumerate(digits[::-1]):
            res += v * 10**i
        res *= msb
        
        return res if res in range(-2**31, 2**31) else 0