class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [float("inf")] * n
        pos = float("-inf")
        for i, char in enumerate(s):
            if char == c:
                pos = i
            res[i] = i - pos
        
        pos = float("inf")

        for j in range(n-1, -1, -1):
            if s[j] == c:
                pos = j
            res[j] = min(res[j], pos-j)

        return res