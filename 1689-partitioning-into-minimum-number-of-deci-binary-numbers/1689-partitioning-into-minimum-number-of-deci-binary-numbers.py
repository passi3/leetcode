class Solution:
    def minPartitions(self, n: str) -> int:
        nums = map(int, list(n))
        return max(nums)