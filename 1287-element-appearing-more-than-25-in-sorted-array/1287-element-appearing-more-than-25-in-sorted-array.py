class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)

        return max([k for k, v in counter.items() if v >= len(arr)*0.25])