class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        for char in s:
            if ord(char) >= 48 and ord(char) <= 57:
                res.pop()
            else:
                res.append(char)
        
        return "".join(res)