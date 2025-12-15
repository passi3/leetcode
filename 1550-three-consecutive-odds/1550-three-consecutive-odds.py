class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
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