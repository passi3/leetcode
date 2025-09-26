class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        rSum = 0
        for num in nums:
            rSum += num
            res.append(rSum)
        return res