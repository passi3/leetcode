class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        cnt = 0
        bins = bin(n)[2:]

        for i in range(len(bins)-1):
            if bins[i] == bins[i+1] and bins[i] == "1":
                cnt += 1

        return cnt == 1