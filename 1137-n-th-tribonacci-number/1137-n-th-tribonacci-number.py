class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1] * (n+1)
        def fibo(n: int) -> int:
            if memo[n] == -1:    
                if n <= 1:
                    memo[n] = n
                elif n == 2:
                    memo[n] = 1
                else:
                    memo[n] = fibo(n-1) + fibo(n-2) + fibo(n-3)    
            return memo[n]
        return fibo(n)
