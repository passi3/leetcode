class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        dictS = dict()

        for char in s:
            dictS[char] = dictS.get(char, 0) + 1

        max_vowel = max((dictS[c] for c in dictS if c in vowels), default=0)
        max_consonant = max((dictS[c] for c in dictS if c not in vowels), default=0)

        return max_vowel + max_consonant