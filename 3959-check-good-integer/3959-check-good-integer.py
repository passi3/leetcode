class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = str(n)
        s = 0
        for c in digits:
            i = int(c)
            s += (i**2) - i
            print(s)
        
        return s >= 50
