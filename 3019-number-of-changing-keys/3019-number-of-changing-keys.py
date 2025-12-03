class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)-1):
            diff = abs(ord(s[i]) - ord(s[i+1]))
            print(diff)
            if diff != 32 and diff != 0:
                cnt += 1
        
        return cnt