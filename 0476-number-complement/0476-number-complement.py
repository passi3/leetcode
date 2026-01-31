class Solution:
    def findComplement(self, num: int) -> int:
        binNum = bin(num)[2:]
        res = ""
        for char in binNum:
            res += "1" if char == "0" else "0"
        
        return int(res, 2)