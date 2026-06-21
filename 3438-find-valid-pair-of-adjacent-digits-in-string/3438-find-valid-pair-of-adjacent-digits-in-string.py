class Solution:
    def findValidPair(self, s: str) -> str:
        for i in range(len(s)-1):
            target = s[i: i+2]
            if len(set(list(target))) == 1:
                continue
            if s.count(target[0]) == int(target[0]) and s.count(target[1]) == int(target[1]):
                return target
        
        return ""