class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []

        tmp = 0
        prev = s[0]
        for i, c in enumerate(s):
            if c == prev:
                tmp += 1
            else:
                if tmp >= 3:
                    res.append([i-tmp, i-1])
                prev = c
                tmp = 1
        
        if tmp >= 3:
            res.append([i-tmp+1, i])
        return res