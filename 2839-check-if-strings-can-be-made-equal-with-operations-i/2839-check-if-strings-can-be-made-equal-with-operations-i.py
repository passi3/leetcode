class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for i in range(2):
            if set(s1[i::2]) != set(s2[i::2]):
                return False
            
        return True