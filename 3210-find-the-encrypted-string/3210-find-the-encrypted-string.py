class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        res = ""
        l = len(s)
        for i in range(l):
            res += s[(i+k)%l]
        
        return res