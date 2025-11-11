class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        countS = s.count("1")
        if countS == 1:
            return "0"*(len(s)-1) + "1"
        elif countS == 2:
            return "1" + "0"*(len(s)-2) + "1"
        else:
            return "1"*(countS - 1) + "0"*(len(s)-countS) + "1"