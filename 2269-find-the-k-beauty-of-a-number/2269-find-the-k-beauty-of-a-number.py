class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        chrNum = str(num)
        for i in range(0, len(chrNum)-k+1):
            if int(chrNum[i:i+k]) != 0 and num % int(chrNum[i:i+k]) == 0:
                res += 1
        return res