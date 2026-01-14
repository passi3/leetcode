class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        res = 0
        counter = Counter(s)
        if len(counter.keys()) <= k:
            return res

        values = sorted(counter.values(), reverse=True)
        while len(values) != k:
            res += values.pop()
        return res
            