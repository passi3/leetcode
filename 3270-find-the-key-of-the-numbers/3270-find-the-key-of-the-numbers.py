class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res = 0
        i = 0
        while num1 > 0 or num2 > 0 or num3 > 0:
            r1, r2, r3 = num1%10, num2%10, num3%10
            ithKey = min(r1, r2, r3)

            res += ithKey * (10**i)
            i += 1
            num1, num2, num3 = num1//10, num2//10, num3//10
        
        return res