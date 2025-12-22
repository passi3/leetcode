class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if len(res) == 0:
                res.append(s[i])
            elif abs(ord(res[-1]) - ord(s[i])) == 32:
                res.pop()
            else:
                res.append(s[i])
        
        return "".join(res)