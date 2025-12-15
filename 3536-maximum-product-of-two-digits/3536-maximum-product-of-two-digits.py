class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n > 0:
            q, r = n//10, n%10
            digits.append(r)
            n = q
        
        digits.sort()
        return digits[-1]*digits[-2]