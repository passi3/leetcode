class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = [0]*len(cost)
        preCost = max(cost)

        for i in range(len(cost)):
            if cost[i] < preCost:
                res[i] = cost[i]
                preCost = cost[i]
            else:
                res[i] = preCost
        
        return res