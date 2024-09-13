class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = [[0] * (n-2) for _ in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                submatrix = [grid[i+x][j:j+3] for x in range(3)]
                max_val = max(max(row) for row in submatrix)
                max_local[i][j] = max_val

        return max_local        
