class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        conseq = 0
        for num in arr:
            print(num)
            if num%2 == 1:
                conseq += 1
            else:
                conseq = 0

            if conseq == 3:
                return True
        
        return False