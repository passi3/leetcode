class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            score = abs(ord(s[i])-ord(s[i+1]))
            print(score)
            sum += score

        return sum