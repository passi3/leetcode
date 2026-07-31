class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = 0
        for i in range(len(number)):
            if number[i] == digit:
                 target = int(number[:i] + number[i+1:])
                 res = max(res, target)
        
        return str(res)