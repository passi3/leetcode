class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        
        for l in s[1:]:
            if stack and l == stack[-1]:
                stack.pop()
            else:
                stack.append(l)
            
        return "".join(stack)