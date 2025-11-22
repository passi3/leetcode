class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        l = len(str(num))

        if l == 1:
            return 1
        
        for i in range(l):
            if num % int(str(num)[i]) == 0:
                cnt += 1
        
        return cnt