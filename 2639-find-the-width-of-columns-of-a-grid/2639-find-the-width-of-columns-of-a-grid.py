class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        res = [0]*n
        for i in range(n):
            res[i] = max(len(str(grid[r][i])) for r in range(m))
        
        return res