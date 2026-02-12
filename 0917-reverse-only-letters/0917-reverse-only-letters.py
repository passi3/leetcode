class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = ""
        letters = [char for char in s if char.isalpha()]
        
        for char in s:
            if char.isalpha():
                res += letters.pop()
            else:
                res += char

        return res