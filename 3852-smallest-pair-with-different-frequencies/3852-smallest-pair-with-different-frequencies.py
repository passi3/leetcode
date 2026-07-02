class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        counter = Counter(nums)
        
        if len(set(counter.values())) < 2:
            return [-1, -1]

        idx0 = min([k for k, v in counter.items()])
        idx1 = min([k for k, v in counter.items() if v != counter[idx0]])
        return [idx0, idx1]