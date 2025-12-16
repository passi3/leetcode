class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hash = dict()
        l = len(nums)
        for num in nums:
            for i in num:
                hash[i] = hash.get(i, 0)+1

        return sorted([k for k, v in hash.items() if v == len(nums)])