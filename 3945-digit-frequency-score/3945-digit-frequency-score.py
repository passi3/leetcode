class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        counter = Counter(str(n))
        
        return sum(int(k) * v for k, v in counter.items())