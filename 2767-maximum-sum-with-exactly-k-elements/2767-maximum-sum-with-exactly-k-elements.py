class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        num = max(nums)
        for i in range(k):
            res += num+i
        return res