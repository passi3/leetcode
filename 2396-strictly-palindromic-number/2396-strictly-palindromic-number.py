class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n-1):
            rep = ""
            target = n
            while target > 0:
                rep += str(target%base)
                target //= base
            if rep != rep[::-1]:
                return False
        
        return True