class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        stack = []
        res = 0
        for char in s:
            stack.append(char)
            if stack.count(char) > 2:
                target = stack.index(char)
                stack = stack[target+1:]
            temp = len(stack)
            if temp > res:
                res = temp

        return res