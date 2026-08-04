class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        s = s.upper().replace("-", "")
        
        while s:
            res.append(s[-k:])
            s = s[:-k]
        
        return "-".join(res[::-1])