class Solution:
    def repeatedCharacter(self, s: str) -> str:
        appeared = {}
        for char in s:
            if char not in appeared:
                appeared[char] = 1
            else:
                return char