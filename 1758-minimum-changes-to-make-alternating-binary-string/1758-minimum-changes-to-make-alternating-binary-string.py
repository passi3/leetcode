class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        s = s.strip()
        startWith0 = 0
        startWith1 = 0
        for i in range(n):
            if i%2 == 0:
                if s[i] != "0":
                    startWith0 += 1
                else:
                    startWith1 += 1
            else:
                if s[i] != "1":
                    startWith0 += 1
                else:
                    startWith1 += 1
        return min(startWith0, startWith1)