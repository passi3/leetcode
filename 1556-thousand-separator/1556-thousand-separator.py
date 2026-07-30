class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ""
        cnt = 0
        for c in str(n)[::-1]:
            if cnt == 3:
                cnt = 0
                res += "."
            res += c
            cnt += 1
        return res[::-1]