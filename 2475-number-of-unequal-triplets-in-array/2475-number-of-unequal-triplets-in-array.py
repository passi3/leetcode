class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res = 0
        cnts = list(Counter(nums).values())
        l = len(cnts)

        for i in range(l-2):
            for j in range(i+1, l-1):
                for k in range(j+1, l):
                    res += cnts[i]*cnts[j]*cnts[k]
        
        return res