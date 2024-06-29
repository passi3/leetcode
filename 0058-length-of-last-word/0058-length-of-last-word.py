class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        l = len(words[-1])
        return l