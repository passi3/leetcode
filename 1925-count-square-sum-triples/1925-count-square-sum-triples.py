class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        squares = set(i*i for i in range(1, n+1))
        
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if i*i + j*j in squares:
                    cnt += 2
        
        return cnt