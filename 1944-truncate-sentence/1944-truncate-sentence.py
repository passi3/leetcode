class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        split_s = s.split()
        return " ".join(split_s[:k])