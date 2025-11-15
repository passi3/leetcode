class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        splitS = s.split()
        for word in splitS:
            res+=word[::-1] + " "
        return res[:-1]