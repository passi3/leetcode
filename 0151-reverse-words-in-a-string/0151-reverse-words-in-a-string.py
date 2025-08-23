class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split()
        reverse_s = split_s[::-1]
        return " ".join(reverse_s)