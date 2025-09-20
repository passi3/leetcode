class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for curr in nums:
            cnt = sum(1 for x in nums if x<curr)
            res.append(cnt)
        return res