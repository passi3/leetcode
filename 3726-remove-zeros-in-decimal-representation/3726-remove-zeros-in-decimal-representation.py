class Solution:
    def removeZeros(self, n: int) -> int:
        res = ""
        n = str(n)
        for i in n:
            if i != "0":
                res += i
        
        return int(res)