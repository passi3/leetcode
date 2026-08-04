class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        pivot = 0
        for d in dimensions:
            diagonal = (d[0]**2 + d[1]**2)**0.5
            if diagonal > pivot:
                res = d[0] * d[1]
                pivot = diagonal
            elif diagonal == pivot:
                res = max(res, d[0]*d[1])
        
        return res