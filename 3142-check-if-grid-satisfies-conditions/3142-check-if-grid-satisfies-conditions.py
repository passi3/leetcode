class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        if len(grid) != 1:
            for i in range(len(grid)-1):
                if grid[i] != grid[i+1]:
                    return False
        
        for i in range(len(grid[0])-1):
            if grid[0][i] == grid[0][i+1]:
                return False
        
        return True