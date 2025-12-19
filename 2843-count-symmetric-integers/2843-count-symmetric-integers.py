class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0

        for i in range(low, high+1):
            iStr = str(i)
            if len(iStr) % 2 == 1:
                continue
            half = len(iStr) // 2
            first, second = iStr[:half], iStr[half:]
            bal = 0
            for j in range(half):
                bal += int(first[j]) - int(second[j])
            
            if bal == 0:
                cnt += 1
        
        return cnt