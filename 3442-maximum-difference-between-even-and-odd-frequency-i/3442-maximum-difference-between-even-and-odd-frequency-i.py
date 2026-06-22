class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        a1 = float('-inf')
        a2 = float('inf')

        for k, v in counter.items():
            if v % 2 == 1:
                a1 = max(a1, v)
            else:
                a2 = min(a2, v)
      
        return a1 - a2