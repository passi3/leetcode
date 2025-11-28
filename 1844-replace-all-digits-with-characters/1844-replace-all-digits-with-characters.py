class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            if i%2 == 0:
                char = s[i]
                res += char
            else:
                digit = int(s[i])
                res += chr(ord(char) + digit)
        
        return res
