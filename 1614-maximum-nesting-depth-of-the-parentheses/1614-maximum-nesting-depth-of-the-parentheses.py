class Solution:
    def maxDepth(self, s: str) -> int:
        
        depth = []
        cnt = 0
        for char in s:
            if char == "(":
                cnt += 1
            elif char == ")":
                depth.append(cnt)
                cnt -= 1

        return max(depth) if len(depth) != 0 else 0