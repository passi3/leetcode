class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        
        while len(s) >= k:
            res.append(s[:k])
            s = s[k:]
        
        l = len(s)

        if l > 0:
            res.append(s + fill*(k-l))
        
        return res