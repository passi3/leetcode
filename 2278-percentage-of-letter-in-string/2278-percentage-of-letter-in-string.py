class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0
        for l in s:
            if l == letter:
                cnt += 1
        return floor(cnt/len(s) * 100)