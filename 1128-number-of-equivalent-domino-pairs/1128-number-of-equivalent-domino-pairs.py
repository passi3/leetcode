class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        counter = Counter()

        for d in dominoes:
            key = tuple(sorted(d))
            counter[key] += 1
        
        for v in counter.values():
            res += v * (v - 1) // 2

        return res