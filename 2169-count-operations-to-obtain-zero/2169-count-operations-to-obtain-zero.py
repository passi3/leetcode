class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 and num2:
            if num1 >= num2:
                t = max(1, num1 // num2)
                num1 -= num2*t
            else:
                t = max(1, num2 // num1)
                num2 -= num1*t
            cnt += t
        return cnt