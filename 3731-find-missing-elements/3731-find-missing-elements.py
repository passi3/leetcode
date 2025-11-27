class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = list(range(min(nums), max(nums)+1))
        for num in nums:
            if num in res:
                res.remove(num)

        return res
