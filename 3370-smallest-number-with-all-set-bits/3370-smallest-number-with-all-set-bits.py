class Solution:
    def smallestNumber(self, n: int) -> int:
        cnt = 1
        while n // 2 >= 1:
            q = n//2
            n = q
            cnt += 1
        
        return 2**cnt - 1