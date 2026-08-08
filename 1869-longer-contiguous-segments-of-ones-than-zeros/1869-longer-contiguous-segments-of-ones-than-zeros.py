class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = zeros = 0
        curr = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                if s[i-1] == "0":
                    zeros = max(zeros, curr)
                else:
                    ones = max(ones, curr)
                curr = 1

        if s[-1] == "0":
            zeros = max(zeros, curr)
        else:
            ones = max(ones, curr)

        return ones > zeros