class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        res = [0]*l
        for i in range(l):
            for j in range(i+1, l):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
                res[i] = prices[i]
            
            if i == l-1:
                res[i] = prices[i]
        return res