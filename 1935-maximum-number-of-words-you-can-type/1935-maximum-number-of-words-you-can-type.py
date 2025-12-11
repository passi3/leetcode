class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        cnt = 0
        brokenSet = set(brokenLetters)
        for word in text:
            if brokenSet - set(word) == brokenSet:
                cnt += 1

        return cnt