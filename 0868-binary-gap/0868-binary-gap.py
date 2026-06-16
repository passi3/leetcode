class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        pp = float('inf')
        curr = 0

        while n > 0:
            if n & 1:
                res = max(res, curr - pp)
                pp = curr

            curr += 1
            n >>= 1

        return res