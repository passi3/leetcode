class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum, digitProduct = 0, 1
        origin = n
        while n > 0:
            q, r = n//10, n%10
            digitSum += r
            digitProduct *= r
            n = q
        
        if origin % (digitSum+digitProduct) == 0:
            return True
        else:
            return False