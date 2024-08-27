from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        result = 0

        for count in freq.values():
            result += count * (count -1) // 2

        return result