class Solution:
    def countCommas(self, n: int) -> int:
        cnt = 0
        while n >= 1000:
            q, r = n // 1000, n % 1000
            cnt += 1000 * (q - 1) + r + 1
            n = q
        return cnt