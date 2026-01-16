class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counter = Counter(str(n))
        return min([int(k) for k,v in counter.items() if v == min(counter.values())])