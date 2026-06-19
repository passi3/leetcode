class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = set("aeiou")
        s = list(s.strip())

        while (s[-1] in vowels):
            s = s[:-1]
            if len(s) == 0:
                return ""
        
        return "".join(s)