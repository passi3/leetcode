class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l =len(mat)
        res = 0
        for i in range(l):
            if l%2 == 1 and i == l//2:
                res += mat[i][i]
            else:
                res += mat[i][i] + mat[i][-i-1]
            print(res)
        return res
