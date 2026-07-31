class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s == "1":
            return True
        
        cnt = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                cnt += 1

        return cnt < 2