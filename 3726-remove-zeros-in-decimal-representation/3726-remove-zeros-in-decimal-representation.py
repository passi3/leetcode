class Solution:
    def removeZeros(self, n: int) -> int:
        res = 0
        residues = []
        while n > 0:
            q, r = n//10, n%10
            if r != 0:
                residues.append(r)
            n = q
        for i, num in enumerate(residues):
            res += num*10**(i)
        
        return res