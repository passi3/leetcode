class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        for i, e1 in enumerate(s):
            for j, e2 in enumerate(t):
                if e2 == e1:
                    result += abs(i-j)
        return result