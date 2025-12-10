class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        sSet = set(s)
        prevCnt = 0
        for char in sSet:
            currCnt = s.count(char)
            if prevCnt ==0:
                prevCnt = currCnt
            else:
                if currCnt != prevCnt:
                    return False
        
        return True