class Solution:
    def minimumFlips(self, n: int) -> int:
        cnt = 0
        nBin = bin(n)[2:]
        
        for i in range(len(nBin)//2):
            if nBin[i] != nBin[-i-1]:
                cnt += 2
        
        return cnt