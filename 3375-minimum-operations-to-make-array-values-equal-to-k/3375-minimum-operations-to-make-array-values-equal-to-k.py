class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numsSet = set(nums)
        
        if min(numsSet) < k:
            return -1
        
        cnt = 0
        if max(numsSet) == k:
            return cnt
        elif k in numsSet:
            cnt = len(numsSet) - 1
        else:
            cnt = len(numsSet)
        
        return cnt