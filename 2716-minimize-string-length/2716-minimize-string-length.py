class Solution:
    def minimizedStringLength(self, s: str) -> int:
        setS = set(s)
        return len(setS)