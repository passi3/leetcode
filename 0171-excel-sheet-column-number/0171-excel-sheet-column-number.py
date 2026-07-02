class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for i, v in enumerate(columnTitle):
            res += (26**(len(columnTitle) - i - 1)) * (ord(v) - ord("A") + 1)
        
        return res