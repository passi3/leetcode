class Solution:
    def greatestLetter(self, s: str) -> str:
        sSet = set(s)
        res = ""

        for char in sSet:
            if char.isupper() and char.lower() in sSet:
                res = max(res, char)
        
        return res