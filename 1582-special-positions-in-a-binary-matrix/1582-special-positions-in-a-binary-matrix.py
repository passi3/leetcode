class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        m, n = len(mat), len(mat[0])

        rSum = [sum(r) for r in mat]
        cSum = [sum(mat[i][j] for i in range(m)) for j in range(n)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rSum[i] == 1 and cSum[j] == 1:
                    res += 1
        
        return res