class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def dividedByThree(n: int) -> bool:
            if n == 1:
                return True
            elif n % 3 == 0:
                return dividedByThree(n // 3)
            return False
        
        if n == 0:
            return False
        return dividedByThree(n)