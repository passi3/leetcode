class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            score = left.count("0") + right.count("1")
            if score > res:
                res = score
        
        return res