class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            q, r = numBottles // numExchange, numBottles % numExchange
            res += q
            numBottles = q + r

        return res