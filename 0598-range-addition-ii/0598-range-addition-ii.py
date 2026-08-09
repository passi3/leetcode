class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        
        a = b = float("inf")
        for op in ops:
            a, b = min(a, op[0]), min(b, op[1])

        return a*b