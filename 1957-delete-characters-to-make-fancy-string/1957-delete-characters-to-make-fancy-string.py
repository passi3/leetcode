class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        last = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == last[-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                last += s[i]

        return last