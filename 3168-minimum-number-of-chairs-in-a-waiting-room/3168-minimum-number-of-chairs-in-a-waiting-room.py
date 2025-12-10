class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = []
        cnt = 0
        for i in range(len(s)):
            if s[i] == "E":
                cnt -= 1
            else:
                cnt += 1
            chairs.append(abs(cnt))
        
        return max(chairs)