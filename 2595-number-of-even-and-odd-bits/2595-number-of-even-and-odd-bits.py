class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0, 0]
        binary = str(bin(n)[2:])[::-1]
        
        for i, v in enumerate(binary):
            if i % 2 == 0 and v == "1":
                res[0] += 1
            elif i % 2 == 1 and v == "1":
                res[1] += 1
        
        return res