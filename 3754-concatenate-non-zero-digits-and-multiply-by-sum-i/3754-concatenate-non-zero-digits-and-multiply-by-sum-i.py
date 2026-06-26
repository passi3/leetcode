class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        x = str(n).replace("0", "")
        s = sum(map(int, x))
        return int(x) * s