class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        digits = []
        while n > 0:
            q, r = n//10, n%10
            digits = [r]+digits
            n = q
        
        for i in range(len(digits)):
            res += digits[i]*(-1)**(i)
        
        return res