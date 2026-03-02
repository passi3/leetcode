class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        prefix = s[:k][::-1]
        return prefix + s[k:]