class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        cost = sorted(cost, reverse=True)
        l = len(cost)
        for i in range(0, l, 3):
            res += cost[i]
            if i + 1 < l:
                res += cost[i+1]
        
        return res