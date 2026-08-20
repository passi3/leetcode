class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        res = []
        seen = []
        k = 0

        for num in nums:
            if num > 0:
                seen = [num] + seen
                k = 0
            else:
                k += 1
                l = len(seen)
                if k <= l:
                    res.append(seen[k-1])
                else:
                    res.append(-1)
        
        return res