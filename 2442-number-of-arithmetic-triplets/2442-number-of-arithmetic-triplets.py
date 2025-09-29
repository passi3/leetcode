class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        numsSet = set(nums)
        res = 0
        for x in nums:
            if x + diff in numsSet and x +2*diff in numsSet:
                res += 1
        return res