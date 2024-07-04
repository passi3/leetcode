class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        step_1 = 2
        step_2 = 1

        for i in range(3, n+1):
            current = step_1 + step_2
            step_2 = step_1
            step_1 = current

        return step_1