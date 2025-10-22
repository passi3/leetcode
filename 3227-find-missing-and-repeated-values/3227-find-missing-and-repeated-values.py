class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        size = len(grid)
        nums = set(range(1, size**2 + 1))
        seen = set()
        
        for row in grid:
            for val in row:
                if val in seen:
                    twice = val
                seen.add(val)
        
        missing = list(nums - seen)[0]
        return [twice, missing]