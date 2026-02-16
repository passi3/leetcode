class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0
        
        res = 0
        stack = []
        binN = bin(n)[2:]
        binK = bin(k)[2:]
        print(binN, binK)
        length = min(len(binN), len(binK))
        if len(binN) > length:
            res += binN[-length-1::-1].count("1")
        elif len(binN) < len(binK):
            return -1
        for i in range(-1, -length-1, -1):
            if binN[i] == "1" and binN[i] != binK[i]:
                res += 1
            elif binN[i] == "0" and binN[i] != binK[i]:
                return -1
        return res