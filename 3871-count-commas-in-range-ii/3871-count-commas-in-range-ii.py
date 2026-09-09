class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        d = 1000

        while d <= n:
            res += n - d + 1
            d *= 1000
        
        return res