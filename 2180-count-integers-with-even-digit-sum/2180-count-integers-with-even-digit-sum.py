class Solution:
    def countEven(self, num: int) -> int:
        res = 0

        for i in range(1, num+1):
            dSum = 0
            while i > 0:
                q, r = i//10, i%10
                i = q
                dSum += r

            if dSum % 2 == 0:
                res += 1
        
        return res