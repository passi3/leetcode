class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        q, r = time // (n-1), time % (n-1)

        return r+1 if q%2==0 else n-r