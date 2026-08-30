class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        cIndices = []
        for i, char in enumerate(s):
            if char == c:
                cIndices.append(i)
        
        for i in range(len(s)):
            dist = min([abs(i-idx) for idx in cIndices])
            res.append(dist)

        return res