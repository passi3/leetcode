class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1]]
        for i in range(1,numRows):
            r = [1]
            for j in range(1, i):
                r.append(l[i-1][j-1] + l[i-1][j])
            r.append(1)
            l.append(r)
        return l