class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_sum = sum(nums)
        res = 0

        for i in range(n):
            suffix_sum -= nums[i]
            remain = n - i - 1

            if remain > 0 and nums[i] > suffix_sum / remain:
                res += 1

        return res