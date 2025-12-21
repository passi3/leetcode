class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        preUpper = 0
        for bracket in brackets:
            if income == 0:
                return res

            earned = (min(bracket[0]-preUpper, income)) 
            preUpper = bracket[0]
            income -= earned
            res += earned * bracket[1] / 100
        
        return res