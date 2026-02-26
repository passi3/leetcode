class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        tol = ((n+1)*n)/2
        for i in range(n+1):
            if i%m == 0:
                tol-=2*i
        return int(tol)