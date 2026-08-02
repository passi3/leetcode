class Solution:
    def countValidPrefixes(self, s: str) -> int:
        l = len(s) + 1
        zeros = [0] * l
        
        for i in range(1, l):
            zeros[i] = zeros[i-1]
            
            if s[i-1] == "0":
                zeros[i] += 1
        
        return sum(1 for i in range(1, l) if abs(i-2*zeros[i]) <= 1)