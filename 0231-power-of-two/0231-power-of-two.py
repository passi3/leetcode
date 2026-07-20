class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def dividedByTwo(n: int) -> bool:
            if n == 1:
                return True
            elif n % 2 == 0:
                return dividedByTwo(n//2)
            return False
        
        if n == 0:
            return False
        return dividedByTwo(n)