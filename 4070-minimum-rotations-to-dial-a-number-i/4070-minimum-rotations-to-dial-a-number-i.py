class Solution:
    def minRotations(self, s: str) -> int:
        res = 0
        curr = 0

        for i in s:
            d = abs(int(i) - curr)
            res += min(d, 10-d)
            curr = int(i)
        
        return res