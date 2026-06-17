class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for num in nums[1:]:
            prefix_sum.append(num + prefix_sum[-1])

        if min(prefix_sum) >= 0:
            return 1
        return abs(min(prefix_sum)) + 1
        