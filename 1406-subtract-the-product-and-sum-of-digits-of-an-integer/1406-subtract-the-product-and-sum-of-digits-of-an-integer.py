class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        length = len(str(n))
        p, s = 1, 0
        if length == 1:
            return 0
        else:
            for i in range(1,length+1):
                q = n // (10**(length - i))
                p *= q
                s += q
                n = n - q*10**(length-i)
        return p - s