class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])

        for c in range(n):
            for r in range(c, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for i in range(n):
            matrix[i].reverse()