class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recur(n: int) -> bool:
            if n == 1:
                return True
            if n <= 0 or n % 4 != 0:
                return False
            return recur(n // 4)
        
        return recur(n)