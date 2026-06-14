class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        
        for row in range(1, len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] <= grid[row - 1][col]:
                    temp = grid[row - 1][col] + 1 - grid[row][col]
                    res += temp
                    grid[row][col] += temp
        
        return res
