class Solution:
    def countMonobit(self, n: int) -> int:
        res = 1
        val = 1
        
        while val <= n:
            val = val * 2 + 1
            res += 1
        
        return res