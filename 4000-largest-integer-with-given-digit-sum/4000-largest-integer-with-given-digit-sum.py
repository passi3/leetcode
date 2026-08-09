class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if 9 * n < s:
            return -1
        
        res = []
        
        for _ in range(n):
            num = min(9, s)
            res.append(str(num))
            s -= num
        return int("".join(res))