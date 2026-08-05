class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        nums = set(range(1, n+1))

        for r in matrix:
            if set(r) != nums:
                return False
        
        for i in range(n):
            if set(matrix[j][i] for j in range(n)) != nums:
                return False
        
        return True