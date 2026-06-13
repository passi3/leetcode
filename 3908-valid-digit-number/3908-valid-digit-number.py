class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return str(n)[1:].count(str(x)) >= 1 and str(n)[0] != str(x)