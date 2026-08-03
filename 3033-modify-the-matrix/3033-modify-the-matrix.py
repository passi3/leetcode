class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        colVal = [0]*n
        
        for c in range(n):
            for r in range(m):
                colVal[c] = max(matrix[r][c], colVal[c])

        for r in range(m):
            for c in range(n):
                target = matrix[r][c]
                if target == -1:
                    matrix[r][c] = colVal[c]
        
        return matrix