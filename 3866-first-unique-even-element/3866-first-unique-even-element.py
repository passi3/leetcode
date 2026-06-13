class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counter = Counter(nums)

        res = [k for k, v in counter.items() if k % 2 == 0 and v == 1]
        return res[0] if len(res) > 0 else -1