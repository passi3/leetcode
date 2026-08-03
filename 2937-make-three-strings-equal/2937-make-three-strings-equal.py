class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if not (s1[0] == s2[0] and s1[0] == s3[0]):
            return -1
        elif s1 == s2 and s1 == s3:
            return 0

        l1, l2, l3 = len(s1), len(s2), len(s3)
        pos = 0
        for i in range(min(l1, l2, l3)):
            if s1[i] == s2[i] and s1[i] == s3[i]:
                pos = i+1
            else:
                break
        
        return l1+l2+l3-3*pos