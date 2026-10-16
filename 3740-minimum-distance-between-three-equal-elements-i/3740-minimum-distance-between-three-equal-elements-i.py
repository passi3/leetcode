class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        counter = defaultdict(list)

        for i, num in enumerate(nums):
            counter[num].append(i)

        if not [k for k, indices in counter.items() if len(indices) >= 3]:
            return -1
        res = float("inf")

        for indices in counter.values():
            for i in range(2, len(indices)):
                d = 2 * (indices[i] - indices[i-2])
                res = min(res, d)
        
        return res