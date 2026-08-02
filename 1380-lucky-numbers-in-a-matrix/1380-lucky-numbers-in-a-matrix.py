class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        for r in range(len(matrix)):
            c = matrix[r].index(min(matrix[r]))
            target = matrix[r][c]
            
            if target == max([mat[c] for mat in matrix]):
                res.append(target)

        return res