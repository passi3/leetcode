class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for r in range(len(grid)):
            res += len([num for num in grid[r] if num < 0])
        
        return res