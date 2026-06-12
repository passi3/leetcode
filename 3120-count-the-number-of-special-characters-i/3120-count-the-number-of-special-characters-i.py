class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        
        for char in set(word):
            if ord(char) >= ord("A") and chr(ord(char) - 32) in word:
                res += 1
        
        return res