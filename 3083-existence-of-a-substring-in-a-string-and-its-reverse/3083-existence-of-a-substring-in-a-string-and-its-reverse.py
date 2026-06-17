class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reverse_s = s[::-1]
        
        for i in range(len(s)-1):
            if reverse_s[i:i+2] in s:
                return True
        
        return False