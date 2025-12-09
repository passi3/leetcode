class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a == 1 or b == 1:
            return 1
        
        factors = set()
        minInt = int(min(a, b))
        maxInt = int(max(a, b))
        for i in range(1, minInt//2 + 1):
            if minInt%i == 0:
                q = minInt // i
                if maxInt%i == 0:
                    factors.add(i)
                if maxInt%q == 0:
                    factors.add(q)
        
        return len(factors)