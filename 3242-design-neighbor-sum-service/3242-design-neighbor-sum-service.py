class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.pos = {}
        for r in range(self.n):
            for c in range(self.n):
                self.pos[grid[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        res = 0
        r, c = self.pos[value]
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                res += self.grid[nr][nc]
        return res

    def diagonalSum(self, value: int) -> int:
        res = 0
        r, c = self.pos[value]
        d = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                res += self.grid[nr][nc]
        return res
        

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)