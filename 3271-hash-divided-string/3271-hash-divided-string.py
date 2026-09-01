class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        for i in range(0, len(s)//k):
            temp = 0
            for ch in s[k*i: k*i + k]:
                temp += ord(ch) - ord('a')
            res += chr(temp%26 + ord('a'))
        
        return res