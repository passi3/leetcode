class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        cnt = 0
        for char in s:
            if char == "L":
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                res += 1
        
        return res