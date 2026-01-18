class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        i = 0
        while n > 0:
            component = (n % 10)*10**i
            if component > 0:
                res = [component] + res
            i += 1
            n = n//10
        return res