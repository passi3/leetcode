class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            digit = num
            while digit > 0:
                q, r = digit//10, digit%10
                digit = q
                if r == 0 or num % r != 0:
                    break
            else:
                res.append(num)
        
        return res
