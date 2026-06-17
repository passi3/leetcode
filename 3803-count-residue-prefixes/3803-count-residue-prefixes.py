class Solution:
    def residuePrefixes(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            if len(set(s[:i+1])) == len(s[:i+1]) % 3:
                res += 1
            
        return res