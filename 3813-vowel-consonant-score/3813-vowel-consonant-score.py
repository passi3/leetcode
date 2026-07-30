class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = "aeiou"
        v, c = 0, 0

        for ch in s:
            if ch.lower() in vowels:
                v += 1
            elif ch.isalpha():
                c += 1

        if c == 0:
            return 0

        return v // c