class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        if len(s) == 1:
            return res
        stack = [s[0]]
        
        for i in range(1, len(s)):
            if s[i] == stack[-1]:
                stack.append(s[i])
            else:
                res = max(res, len(stack))
                stack = [s[i]]
        
        return max(res, len(stack))